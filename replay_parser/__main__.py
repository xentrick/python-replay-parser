#!/usr/bin/env python3

import argparse
import logging
import struct
import sys
from pathlib import Path

from replay_parser.parser import ReplayParser

logging.basicConfig(level=logging.INFO)
log = logging.getLogger()

if __package__ is None and not hasattr(sys, "frozen"):
    import os.path

    path = os.path.realpath(os.path.abspath(__file__))
    sys.path.insert(0, os.path.dirname(os.path.dirname(path)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Rocket League Replay Parser")
    parser.add_argument("replay", help="Replay file location")
    parser.add_argument(
        "-d",
        "--debug",
        dest="debug",
        action="store_true",
        default=False,
        required=False,
        help="Turn on debug mode",
    )
    parser.add_argument(
        "-n",
        "--net-stream",
        dest="netstream",
        action="store_true",
        default=False,
        help="Parse network stream (Warning: Very expensive)",
    )
    argv = parser.parse_args()

    debug: bool = argv.debug
    replay_name: str = argv.replay

    if debug:
        log.setLevel(logging.DEBUG)
        log.debug(f"DEBUG: {debug}")

    if not replay_name.endswith(".replay"):
        sys.exit(f"{replay_name} does not appear to be a valid replay file")

    if not Path(replay_name).is_file():
        sys.exit(f"{replay_name} does not exist...")

    with open(replay_name, "rb") as replay_file:
        try:
            rparser = ReplayParser(debug=debug)
            results = rparser.parse(replay_file, replay_name)
        except IOError as e:
            print(e)
        except struct.error as e:
            print(e)
        except Exception as e:
            print(e)
