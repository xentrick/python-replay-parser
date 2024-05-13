import logging
from dataclasses import dataclass

from replay_parser import util
from replay_parser.type import PathLike

log = logging.getLogger(__name__)


@dataclass
class ActorState:
    id: int
    # state: ActorStateState
    unknown1: bool
    name_id: int
    type_id: int
    class_id: int


@dataclass
class Frame:
    number = int
    time: float
    delta: float
    bit_length: int
    actors: list[ActorState]

    @classmethod
    def parse(cls, fd: PathLike) -> "Frame":
        time = util.read_float(fd, 4)
        delta = util.read_float(fd, 4)
        log.debug(f"Frame Time: {time}")
        log.debug(f"Frame Delta: {delta}")

        return cls(
            time,
            delta,
        )
