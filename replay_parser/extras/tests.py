from ..replay_parser import ReplayParser

import os
import unittest


class TestReplayParser(unittest.TestCase):

    def test_example_replays(self):
        parser = ReplayParser()

        for filename in os.listdir('replay_parser/extras/example_replays'):
            with open('replay_parser/extras/example_replays/{}'.format(filename)) as f:
                response = parser.parse(f)

                self.assertIsInstance(response, dict)

if __name__ == '__main__':
    unittest.main()
