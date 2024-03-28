from dataclasses import dataclass

from replay_parser.models.footer import Footer
from replay_parser.models.header import Header


@dataclass
class Replay:
    header: Header
    netstream: bytes | None
    footer: Footer
