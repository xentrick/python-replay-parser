from dataclasses import dataclass

from replay_parser.models.footer import Footer
from replay_parser.models.header import Header, KeyFrame
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

    @property
    def goals(self) -> PropertyValue | None:
        return self.header.get_property("Goals")

    @property
    def keyframes(self) -> list[KeyFrame]:
        return self.header.keyframes

    @property
    def levels(self) -> list[str]:
        return self.header.levels
