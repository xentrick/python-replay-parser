import io
import logging
import os

from replay_parser import models
from replay_parser.exceptions import CorruptReplay
from replay_parser.type import PathLike

log = logging.getLogger(__name__)


class ReplayParser:
    def __init__(self, debug: bool = False):
        self.debug = debug
        if self.debug:
            log.setLevel(logging.DEBUG)
            log.debug("Debug mode: ON")
        else:
            log.setLevel(logging.INFO)

    def parse(
        self,
        replay_file: PathLike,
        net_stream: bool = False,
    ) -> models.Replay:
        # Work out what type of file we're dealing with.
        if isinstance(replay_file, bytes) or hasattr(replay_file, "read"):
            fd = replay_file
        elif hasattr(replay_file, "file"):
            fd = open(replay_file.file.path, "rb")
        elif isinstance(replay_file, str):
            fd = open(replay_file, "rb")
        else:
            raise TypeError("Unable to determine file type.")

        # Get bounds
        fd.seek(0, io.SEEK_END)
        file_size = fd.tell()
        log.debug(f"File Size: {file_size}")
        fd.seek(0, io.SEEK_SET)

        # Header
        hdr = models.Header.parse(fd)

        bv = hdr.build_version
        log.debug(f"hdr.BuildVersion: {bv}")

        # Jump to Footer first
        net_data_start = fd.tell()

        if (net_data_start + hdr.network_stream_length) > file_size:
            raise CorruptReplay("Net stream data length exceeds file size.")

        log.debug(f"Skipping to footer... Net Data Start: {net_data_start}")
        fd.seek(hdr.network_stream_length, os.SEEK_CUR)

        # Parse footer
        footer_start = fd.tell()
        log.debug(f"Footer Start: {footer_start}")
        footer = models.Footer.parse(fd)
        # log.debug(f"Footer: {footer}")

        # Net stream
        network_stream = None
        if net_stream:
            fd.seek(net_data_start)
            network_stream = self.parse_net_stream(fd, hdr, footer)

        fd.close()

        return models.Replay(header=hdr, netstream=network_stream, footer=footer)

    def parse_net_stream(
        self, fd: PathLike, header: models.Header, footer: models.Footer
    ):
        # f = models.Frame.parse(fd)
        # from pprint import pformat
        # log.debug(f"Frame: {f}")
        raise NotImplementedError("Net stream parsing is not supported yet.")
