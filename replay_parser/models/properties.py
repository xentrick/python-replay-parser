import json
import logging
from dataclasses import dataclass
from enum import StrEnum
from typing import TYPE_CHECKING, TypeVar

from replay_parser import util
from replay_parser.type import PathLike

if TYPE_CHECKING:
    from replay_parser.models.header import Version

log = logging.getLogger(__name__)


PropertyValue = TypeVar("PropertyValue", int, str, float, list, bool)


def read_properties(replay_file, version: "Version"):
    results = {}
    while True:
        prop = Property.parse(replay_file, version=version)

        if prop:
            results[prop.name] = prop.value
        else:
            # log.debug(f"Property List:\n\n{json.dumps(results, indent=4)}")
            return results


class PropertyType(StrEnum):
    Int = "IntProperty"
    Str = "StrProperty"
    Name = "NameProperty"
    Float = "FloatProperty"
    Array = "ArrayProperty"
    Byte = "ByteProperty"
    QWord = "QWordProperty"
    Bool = "BoolProperty"


@dataclass
class Property:
    name: str
    type: PropertyType
    unknown_001: int
    value: PropertyValue

    @classmethod
    def parse(cls, fd: PathLike, version: "Version"):
        # log.debug("\tProperty")

        # len = util.read_integer(fd)
        # log.debug(f"\t\tplen: {len}")

        name = util.read_string8(fd)
        log.debug(f"\t\tName: {name}")
        if name in ("None", "\0\0\0None"):
            return None

        ptype = PropertyType(util.read_string8(fd))
        log.debug(f"\t\tptype: {ptype}")

        unk = util.read_integer(fd, 8)
        # log.debug(f"\t\tUnk: {unk}")

        match ptype:
            case PropertyType.Int:
                value = util.read_integer(fd, 4)
            case PropertyType.Str:
                value = util.read_string16(fd)
            case PropertyType.Name:
                value = util.read_string16(fd)
            case PropertyType.Float:
                value = util.read_float(fd, 4)
            case PropertyType.Array:
                alen = util.read_integer(fd, 4)
                log.debug(f"PropertyArray Len: {alen}")
                value = []
                for _ in range(alen):
                    proplist = read_properties(fd, version)
                    value.append(proplist)
                log.debug(f"ArrayProperty Values:\n\n{json.dumps(value, indent=4)}")
            case PropertyType.Byte:
                key = util.read_string8(fd)
                if key in ("OnlinePlatform_Steam", "OnlinePlatform_PS4"):
                    value = None
                else:
                    value = util.read_string8(fd)
            case PropertyType.QWord:
                value = util.read_integer(fd, 8)
            case PropertyType.Bool:
                if (
                    version.engine_version == 0
                    and version.licensee_version == 0
                    and version.net_version == 0
                ):
                    value = util.read_integer(fd, 4)
                else:
                    value = bool(util.read_integer(fd, 1))

        # log.debug(f"\t\tValue: {value}")

        return cls(name, ptype, unk, value)
