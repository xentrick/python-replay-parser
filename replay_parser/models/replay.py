from dataclasses import dataclass

from replay_parser.models.footer import Footer
from replay_parser.models.header import Header
from replay_parser.models.properties import PropertyValue


@dataclass
class Replay:
    header: Header
    netstream: bytes | None
    footer: Footer

    @property
    def map_code(self) -> PropertyValue | None:
        return self.header.get_property("MapName")

    @property
    def player_stats(self) -> PropertyValue | None:
        return self.header.get_property("PlayerStats")
