import json
import logging
from dataclasses import dataclass
from typing import IO

from replay_parser import util
from replay_parser.models.properties import PropertyEncoder, read_properties

log = logging.getLogger(__name__)


@dataclass
class KeyFrame:
    time: float
    frame: int
    file_position: int

    @classmethod
    def parse(cls, fd: IO[bytes]):
        time = util.read_float(fd, 4)
        frame = util.read_integer(fd, 4)
        file_pos = util.read_integer(fd, 4)

        log.debug("KeyFrame:")
        log.debug(f"\t\tTime: {time}")
        log.debug(f"\t\tFrame: {frame}")
        log.debug(f"\t\tFile Position: {file_pos}")

        return cls(time, frame, file_pos)


@dataclass
class Version:
    engine_version: int
    licensee_version: int
    net_version: int

    @classmethod
    def parse(cls, fd: IO[bytes]) -> "Version":
        engine = util.read_integer(fd, 4)
        licensee = util.read_integer(fd, 4)

        if engine >= 866 and licensee >= 18:
            net = util.read_integer(fd)
        else:
            net = 0

        log.debug("\tVersion Structure")
        log.debug(f"\t\tEngine: {engine}")
        log.debug(f"\t\tLicensee: {licensee}")
        log.debug(f"\t\tNet: {net}")

        return cls(engine, licensee, net)


@dataclass
class Header:
    length: int
    crc: int
    version: Version
    type: str
    properties: dict[str, int | str | float | list | bool]
    eof_length: int
    eof_crc: int
    levels: list[str]
    keyframes: list[KeyFrame]
    network_stream_length: int

    def get_property(self, name: str) -> int | str | float | list | bool | None:
        return self.properties.get(name)

    @property
    def build_version(self) -> str | None:
        bv = self.properties.get("BuildVersion")
        if not isinstance(bv, str):
            return None
        return bv

    @classmethod
    def parse(cls, fd: IO[bytes]) -> "Header":
        log.debug("Header Structure")

        hdrlen = util.read_integer(fd, 4)
        crc = util.read_integer(fd, 4)
        log.debug(f"\tHdr Len: {hdrlen}")
        log.debug(f"\tCRC: {crc}")

        version = Version.parse(fd)

        # log.info(f"FTell: {fd.tell()}")

        rtype = util.read_string8(fd)
        log.debug(f"\tReplayType: {rtype}")

        properties = read_properties(fd, version=version)
        log.debug(
            f"Properties:\n{json.dumps(properties, indent=4, cls=PropertyEncoder)}"
        )

        # TODO: Extract BuildVersion

        eof_len = util.read_integer(fd, 4)
        eof_crc = util.read_integer(fd, 4)
        log.debug(f"\tEOF Len: {eof_len}")
        log.debug(f"\tEOF CRC: {eof_crc}")

        lvl_count = util.read_integer(fd, 4)
        log.debug(f"\tLevel Count: {lvl_count}")
        levels = []
        for _ in range(lvl_count):
            lvl = util.read_string8(fd)
            log.debug(f"\t\tLevel: {lvl}")
            levels.append(lvl)

        key_count = util.read_integer(fd, 4)
        log.debug(f"\tKeyFrame Count: {key_count}")
        keyframes = []
        for _ in range(key_count):
            kframe = KeyFrame.parse(fd)
            keyframes.append(kframe)

        net_stream_len = util.read_integer(fd, 4)
        log.debug(f"\tNetwork Stream Length: {net_stream_len}")

        return cls(
            hdrlen,
            crc,
            version,
            rtype,
            properties,
            eof_len,
            eof_crc,
            levels,
            keyframes,
            net_stream_len,
        )
