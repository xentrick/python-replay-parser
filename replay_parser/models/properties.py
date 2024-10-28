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
            # if prop.name == "None":
            #     break
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
    Struct = "StructProperty"


@dataclass
class Property:
    name: str
    type: PropertyType
    length: int
    idx: int
    value: int | str | float | list | bool
    struct_name: str | None = None

    def __str__(self) -> str:
        return f"""Name: {self.name}
Type: {self.type}
Length: {self.length}
Index: {self.idx}
StructName: {self.struct_name}
Value: {self.value}"""

    @classmethod
    def parse(cls, fd: PathLike, version: "Version"):
        # log.debug("\tProperty")

        # len = util.read_integer(fd)
        # log.debug(f"\t\tplen: {len}")

        # Property Name
        name = util.read_string8(fd)
        log.debug(f"\t\tName: {name}")
        if name in ("None", "\0\0\0None"):
            log.debug("NoneType Property Found. Ending parse.")
            return

        # Property Type
        ptype = PropertyType(util.read_string8(fd))
        log.debug(f"\t\tpType: {ptype}")

        # Data Length
        length = util.read_integer(fd, 4)
        log.debug(f"\t\tLength: {length}")

        # Array Index
        idx = util.read_integer(fd, 4)
        log.debug(f"\t\tIndex: {idx}")

        structName = None

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
                    log.debug(f"ArrayProperty Value: {proplist}")
                    value.append(proplist)
                log.debug(
                    f"ArrayProperty Values:\n\n{json.dumps(value, indent=4, cls=PropertyEncoder)}"
                )
            case PropertyType.Byte:
                key = util.read_string8(fd)
                log.debug(f"ByteProperty->Key: {key}")
                if key == "None":
                    # Who knows?
                    value = util.read_byte(fd)
                elif key in ("OnlinePlatform_Steam", "OnlinePlatform_PS4"):
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
            case PropertyType.Struct:
                log.debug("StructProperty found")
                structName = util.read_string8(fd)
                log.debug(f"Struct Name: {structName}")

                # Value is a list of struct fields
                value = []
                while True:
                    struct = Property.parse(fd, version)
                    if not struct:
                        log.debug("Ending StuctProperty parse.")
                        break
                    value.append(struct)

                # value = read_properties(fd, version)
                # value = util.read_string8(fd)
                # log.debug(f"value: {value}")

        log.debug(f"\t\tValue: {value}")

        return cls(name, ptype, length, idx, value, structName)


class PropertyEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__
