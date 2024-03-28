import logging
import os

from replay_parser import models
from replay_parser.type import PathLike

log = logging.getLogger(__name__)


class ReplayParser:
    def __init__(self, debug: bool = False):
        self.debug = debug
        if self.debug:
            log.setLevel(logging.DEBUG)
            log.debug("Debug mode: ON")

    def parse(
        self, replay_file: PathLike, filename: str | None = None, deep: bool = True
    ):
        # Work out what type of file we're dealing with.
        if hasattr(replay_file, "read"):
            replay_file.seek(0)
            fd = replay_file
        elif hasattr(replay_file, "file"):
            fd = open(replay_file.file.path, "rb")
        elif isinstance(replay_file, str):
            fd = open(replay_file, "rb")
        else:
            raise TypeError("Unable to determine file type.")

        # Header
        hdr = models.Header.parse(fd)

        # Jump to Footer first
        net_data_start = fd.tell()
        log.debug(f"Skipping to footer... Net Data Start: {net_data_start}")
        fd.seek(hdr.network_stream_length, os.SEEK_CUR)

        # Parse footer
        footer_start = fd.tell()
        log.debug(f"Footer Start: {footer_start}")
        footer = models.Footer.parse(fd)
        log.debug(f"Footer: {footer}")

        fd.close()

        return footer  # Fix to replay structure
