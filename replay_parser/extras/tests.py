from replay_parser import ReplayParser

import struct
import unittest


class TestReplayParser(unittest.TestCase):

    def test_104_replay(self):
        parser = ReplayParser()

        with open('extras/example_replays/1.04.replay') as f:
            response = parser.parse(f)
            self.assertIsInstance(response, dict)
            self.assertEqual(response['header']['Id'], '0AB18BAB4CCE97201B7753A84B358D48')

    def test_105_replay(self):
        parser = ReplayParser()

        with open('extras/example_replays/1.05.replay') as f:
            response = parser.parse(f)
            self.assertIsInstance(response, dict)
            self.assertEqual(response['header']['Id'], '56E7708C45ED1CF3B9E51EBF1ADF4431')

    def test_broken_replay(self):
        parser = ReplayParser()

        with open('extras/example_replays/broken.replay') as f:
            with self.assertRaises(struct.error):
                parser.parse(f)

if __name__ == '__main__':
    unittest.main()
