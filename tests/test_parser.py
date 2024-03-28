import os
import struct
import sys
from io import BytesIO, StringIO

import pytest

from replay_parser import util
from replay_parser.parser import ReplayParser


class TestReplayParser:
    folder_path = "{}/replays/".format(os.path.dirname(os.path.realpath(__file__)))

    def test_ensure_all_replays_tested(self):
        for filename in os.listdir(self.folder_path):
            if not filename.endswith(".replay"):
                continue

            # Generate a test name.
            filename = "test_{}_replay".format(
                filename.replace(".replay", "")
                .replace(".", "")
                .replace("-", "_")
                .lower()
            )

            assert hasattr(self, filename)

    def test_104_replay(self):
        """
        A replay from version 1.04.
        """

        parser = ReplayParser()

        with open(self.folder_path + "1.04.replay", "rb") as f:
            response = parser.parse(f)
            assert isinstance(response, dict)
            assert response["header"]["Id"] == "0AB18BAB4CCE97201B7753A84B358D48"
            assert "PlayerStats" not in response["header"]

    def test_105_replay(self):
        """
        A replay from version 1.05.
        """

        parser = ReplayParser()

        with open(self.folder_path + "1.05.replay", "rb") as f:
            response = parser.parse(f)
            assert isinstance(response, dict)
            assert response["header"]["Id"] == "56E7708C45ED1CF3B9E51EBF1ADF4431"
            assert "PlayerStats" not in response["header"]

    def test_106_replay(self):
        """
        A replay from version 1.05.
        """

        parser = ReplayParser()

        with open(self.folder_path + "1.06.replay", "rb") as f:
            response = parser.parse(f)
            assert isinstance(response, dict)
            assert response["header"]["Id"] == "E64C704042DFFF5E92F76EB9217B6422"
            assert "PlayerStats" in response["header"]

    def test_106_2_replay(self):
        """
        A replay from version 1.05, with bots.
        """

        parser = ReplayParser()

        with open(self.folder_path + "1.06_2.replay", "rb") as f:
            response = parser.parse(f)
            assert isinstance(response, dict)
            assert response["header"]["Id"] == "BBA60356493A53E6D4D7ADBA4E5D99B9"
            assert "PlayerStats" in response["header"]

    def test_108_replay(self):
        """
        A replay from version 1.05.
        """

        parser = ReplayParser()

        with open(self.folder_path + "1.08.replay", "rb") as f:
            response = parser.parse(f)
            assert isinstance(response, dict)
            assert response["header"]["Id"] == "9E4289CA4109CEF9FF2185AD861445EB"
            assert "PlayerStats" in response["header"]

    def test_110_replay(self):
        """
        A replay from version 1.05.
        """

        parser = ReplayParser()

        with open(self.folder_path + "1.10.replay", "rb") as f:
            response = parser.parse(f)
            assert isinstance(response, dict)
            assert response["header"]["Id"] == "BF5FF16E41A5E76552888FB1F0CE6990"
            assert "PlayerStats" in response["header"]

    def test_111_replay(self):
        """
        A replay from version 1.05.
        """

        parser = ReplayParser()

        with open(self.folder_path + "1.11.replay", "rb") as f:
            response = parser.parse(f)
            assert isinstance(response, dict)
            assert response["header"]["Id"] == "158DEE6541E83F745C12E8A3EE72B479"
            assert "PlayerStats" in response["header"]

    def test_broken_replay(self):
        """
        This replay file was purposefully broken by deleting a large portion
        of the data.
        """

        parser = ReplayParser()

        with open(self.folder_path + "broken.replay", "rb") as f, pytest.raises(
            struct.error
        ):
            parser.parse(f)

    def test_keyframes_missing_replay(self):
        """
        For some reason, this replay is missing the key frames from when goals
        were scored, so that data is not available to a parser. This is a good
        test to ensure the parser can handle odd scenarios.
        """

        parser = ReplayParser()

        with open(self.folder_path + "keyframes_missing.replay", "rb") as f:
            response = parser.parse(f)
            assert isinstance(response, dict)
            assert response["header"]["Id"] == "50D5031342FF90D9F25BE5A0152E56B8"

    def test_2s_replay(self):
        """
        This is the shortest possible replay, at only 2 seconds long. It was
        created by loading in to a split-screen 2v2 ranked match and forfeiting
        as soon as the action was available.
        """

        parser = ReplayParser()

        with open(self.folder_path + "2s.replay", "rb") as f:
            response = parser.parse(f)
            assert isinstance(response, dict)
            assert response["header"]["Id"] == "016D2CB946676AFDC11D29BFD84C9CB3"

    def test_limited_action_replay(self):
        """
        This is a very simple replay which doesn't have much action taking place.
        """

        parser = ReplayParser()

        with open(self.folder_path + "limited_action.replay", "rb") as f:
            response = parser.parse(f)
            assert isinstance(response, dict)
            assert response["header"]["Id"] == "C6ADF673457FE9B7B2A82DAB36E8FF86"

    def test_score_wrong_replay(self):
        """
        This is a very replay which has some weird goal header data.
        """

        parser = ReplayParser()

        with open(self.folder_path + "score_wrong.replay", "rb") as f:
            response = parser.parse(f)
            assert isinstance(response, dict)
            assert response["header"]["Id"] == "B76567B84633D0D9CD8D4597DB0CAB30"

    def test_file_attr(self):
        class Obj:
            class File:
                path = self.folder_path + "2s.replay"

            file = File()

        parser = ReplayParser()

        response = parser.parse(Obj())
        assert isinstance(response, dict)
        assert response["header"]["Id"] == "016D2CB946676AFDC11D29BFD84C9CB3"

    def test_file_str(self):
        parser = ReplayParser(debug=True)
        response = parser.parse(self.folder_path + "2s.replay")

        assert isinstance(response, dict)
        assert response["header"]["Id"] == "016D2CB946676AFDC11D29BFD84C9CB3"

    def test_file_exception(self):
        parser = ReplayParser()

        with pytest.raises(TypeError):
            parser.parse(None)

    def test_debug_bits(self):
        data = StringIO()
        data.write("\u0001")
        data.seek(0)

        stdout = sys.stdout
        sys.stdout = StringIO()

        bits = util.debug_bits(data)

        output = sys.stdout.getvalue()
        sys.stdout.close()
        sys.stdout = stdout

        assert (
            output
            == """1.......
.0......
..0.....
...0....
....0...
.....0..
......0.
.......0
"""
        )
        assert bits == (1, 0, 0, 0, 0, 0, 0, 0)

    def test_debug_bits_with_labels(self):
        data = StringIO()
        data.write("\u0001")
        data.seek(0)

        stdout = sys.stdout
        sys.stdout = StringIO()

        bits = util.debug_bits(data, ["A", "B", "C", "D", "E", "F", "G", "H"])

        output = sys.stdout.getvalue()
        sys.stdout.close()
        sys.stdout = stdout

        assert (
            output
            == """1....... = A: Not set
.0...... = B: Not set
..0..... = C: Not set
...0.... = D: Not set
....0... = E: Not set
.....0.. = F: Not set
......0. = G: Not set
.......0 = H: Not set
"""
        )
        assert bits == (1, 0, 0, 0, 0, 0, 0, 0)

    def test_read_bit(self):
        assert util.read_bit("\u0001", 0) == 1
        assert util.read_bit("\u0001", 1) == 0
        assert util.read_bit("\u0001", 2) == 0
        assert util.read_bit("\u0001", 3) == 0
        assert util.read_bit("\u0001", 4) == 0
        assert util.read_bit("\u0001", 5) == 0
        assert util.read_bit("\u0001", 6) == 0
        assert util.read_bit("\u0001", 7) == 0

    def test_pretty_byte_string(self):
        response = util.pretty_byte_string("\u0000\u0001\u0002\u0003")

        assert response == "00 01 02 03"

    def test_read_integer(self):
        data = BytesIO()
        data.write(b"\x01\x02\x03\x04\x05\x06\x07\x08")

        # Signed integers.
        data.seek(0)
        response = util.read_integer(data, 1)
        assert response == 1

        data.seek(0)
        response = util.read_integer(data, 2)
        assert response == 513

        data.seek(0)
        response = util.read_integer(data, 4)
        assert response == 67305985

        data.seek(0)
        response = util.read_integer(data, 8)
        assert response == 578437695752307201

    def test_sniff_bytes_0_bytes(self):
        data = BytesIO()
        data.write(b"")

        stdout = sys.stdout
        sys.stdout = StringIO()

        data.seek(0)
        util.sniff_bytes(data, 0)

        output = sys.stdout.getvalue()
        sys.stdout.close()
        sys.stdout = stdout

        assert (
            output
            == """**** BYTES ****
Bytes: \n\
Size: 0\n\
String: b''\n\
"""
        )

    def test_sniff_bytes_1_byte(self):
        data = BytesIO()
        data.write(b"\x31")

        stdout = sys.stdout
        sys.stdout = StringIO()

        data.seek(0)
        util.sniff_bytes(data, 1)

        output = sys.stdout.getvalue()
        sys.stdout.close()
        sys.stdout = stdout

        assert (
            output
            == """**** BYTES ****
Bytes: 31
Size: 1
String: b'1'
"""
        )

    def test_sniff_bytes_2_bytes(self):
        data = BytesIO()
        data.write(b"\x31\x32")

        stdout = sys.stdout
        sys.stdout = StringIO()

        data.seek(0)
        util.sniff_bytes(data, 2)

        output = sys.stdout.getvalue()
        sys.stdout.close()
        sys.stdout = stdout

        assert (
            output
            == """**** BYTES ****
Bytes: 31 32
Size: 2
Short: Signed: (12849,) Unsigned: (12849,)
"""
        )

    def test_sniff_bytes_3_bytes(self):
        data = BytesIO()
        data.write(b"\x31\x32\x33")

        stdout = sys.stdout
        sys.stdout = StringIO()

        data.seek(0)
        util.sniff_bytes(data, 3)

        output = sys.stdout.getvalue()
        sys.stdout.close()
        sys.stdout = stdout

        assert (
            output
            == """**** BYTES ****
Bytes: 31 32 33
Size: 3
String: b'123'
"""
        )

    def test_sniff_bytes_4_bytes(self):
        data = BytesIO()
        data.write(b"\x31\x32\x33\x34")

        stdout = sys.stdout
        sys.stdout = StringIO()

        data.seek(0)
        util.sniff_bytes(data, 4)

        output = sys.stdout.getvalue()
        sys.stdout.close()
        sys.stdout = stdout

        assert (
            output
            == """**** BYTES ****
Bytes: 31 32 33 34
Size: 4
Integer: Signed: (875770417,), Unsigned: (875770417,)
Float: (1.6688933612840628e-07,)
String: b'1234'
"""
        )
