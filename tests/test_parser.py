import os
import sys
from io import BytesIO, StringIO

from replay_parser import util
from replay_parser.models import Replay
from replay_parser.parser import ReplayParser


class TestReplayParser:
    folder_path = "{}/replays/".format(os.path.dirname(os.path.realpath(__file__)))

    def test_104_replay(self):
        """
        A replay from version 1.04.
        """

        parser = ReplayParser()

        with open(self.folder_path + "2.45.replay", "rb") as f:
            replay = parser.parse(f)
            assert isinstance(replay, Replay)

            goals = replay.goals
            assert len(goals) == 4

            stats = replay.player_stats
            assert len(stats) == 6

            assert len(replay.keyframes) == 36

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
