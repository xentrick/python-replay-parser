import json
import logging
from dataclasses import dataclass

from replay_parser import util
from replay_parser.models.mapping import RELATIONS
from replay_parser.type import PathLike

log = logging.getLogger(__name__)


NORMALS = [
    "TheWorld:PersistentLevel.BreakOutActor_Platform_TA",
    "TheWorld:PersistentLevel.CrowdActor_TA",
    "TheWorld:PersistentLevel.CrowdManager_TA",
    "TheWorld:PersistentLevel.InMapScoreboard_TA",
    "TheWorld:PersistentLevel.VehiclePickup_Boost_TA",
    "TheWorld:PersistentLevel.HauntedBallTrapTrigger_TA",
    "TheWorld:PersistentLevel.PlayerStart_Platform_TA",
    "TheWorld:PersistentLevel.GoalVolume_TA",
    "TheWorld:PersistentLevel.GoalVolume_Hoops_TA",
    "Archetypes.Teams.Team",
]


def normalize_object(object: str) -> str:
    for normal in NORMALS:
        if normal in object:  # `normal` is a substring of `object`
            return normal
    return object


@dataclass
class DebugString:
    frame: int
    username: str
    text: str

    @classmethod
    def parse(cls, fd: PathLike) -> "DebugString":
        frame = util.read_integer(fd, 4)
        user = util.read_string16(fd)
        text = util.read_string16(fd)
        return cls(frame, user, text)


@dataclass
class TickMark:
    descriptioin: str
    frame: int

    @classmethod
    def parse(cls, fd: PathLike) -> "TickMark":
        desc = util.read_string16(fd)
        frame = util.read_integer(fd, 4)
        return cls(desc, frame)


@dataclass
class FooterClass:
    class_name: str
    object_id: int

    @classmethod
    def parse(cls, fd: PathLike) -> "FooterClass":
        name = util.read_string8(fd)
        obj_id = util.read_integer(fd, 4)
        return cls(name, obj_id)


@dataclass
class ClassNetCacheProperty:
    object_id: int
    parent_id: int

    @classmethod
    def parse(cls, fd: PathLike) -> "ClassNetCacheProperty":
        obj_id = util.read_integer(fd, 4)
        parent_id = util.read_integer(fd, 4)
        return cls(obj_id, parent_id)


@dataclass
class ClassNetCacheEntry:
    object_id: int
    parent_id: int
    cache_id: int
    properties: list[ClassNetCacheProperty]

    @classmethod
    def parse(cls, fd: PathLike) -> "ClassNetCacheEntry":
        obj_id = util.read_integer(fd, 4)
        parent_id = util.read_integer(fd, 4)
        cache_id = util.read_integer(fd, 4)

        props = []
        prop_count = util.read_integer(fd, 4)
        for _ in range(prop_count):
            p = ClassNetCacheProperty.parse(fd)
            props.append(p)

        # log.debug(f"ClassNetCacheProperties:\n\n{props}")

        return cls(obj_id, parent_id, cache_id, props)


@dataclass
class Footer:
    debug_strings: list[DebugString]
    tick_marks: list[TickMark]
    packages: list[str]
    objects: list[str]
    names: list[str]
    classes: list[FooterClass]
    class_net_cache: list

    @classmethod
    def parse(cls, fd: PathLike) -> "Footer":
        log.debug("Footer Structure")

        dbg_strings = []
        c = util.read_integer(fd, 4)
        for _ in range(c):
            dstr = DebugString.parse(fd)
            dbg_strings.append(dstr)

        log.debug(f"Debug Strings:\n\n{dbg_strings}")

        ticks = []
        c = util.read_integer(fd, 4)
        for _ in range(c):
            tm = TickMark.parse(fd)
            ticks.append(tm)

        log.debug(f"Ticks:\n\n{ticks}")

        packages = []
        c = util.read_integer(fd, 4)
        for _ in range(c):
            p = util.read_string16(fd)
            packages.append(p)

        log.debug(f"Packages:\n\n{packages}")

        obj_list = []
        c = util.read_integer(fd, 4)
        for _ in range(c):
            obj = normalize_object(util.read_string16(fd))
            obj_list.append(obj)

        log.debug(f"Objects:\n\n{json.dumps(obj_list, indent=4)}")

        names = []
        c = util.read_integer(fd, 4)
        for _ in range(c):
            n = util.read_string16(fd)
            names.append(n)

        log.debug(f"Names:\n\n{names}")

        classes = []
        c = util.read_integer(fd, 4)
        for _ in range(c):
            fclass = FooterClass.parse(fd)
            classes.append(fclass)

        log.debug(f"Classes:\n\n{classes}")

        cnet_list = []
        c = util.read_integer(fd, 4)
        for _ in range(c):
            cnet = ClassNetCacheEntry.parse(fd)
            cnet_list.append(cnet)

        log.debug(f"ClassNetCacheEntry:\n\n{cnet_list}")

        format_class_net_cache(cnet_list, classes)

        return cls(dbg_strings, ticks, packages, obj_list, names, classes, cnet_list)


# Footer: 1686143 (1346610a...)
def format_class_net_cache(
    class_net_cache: list[ClassNetCacheEntry],
    classes: list[FooterClass],
    object_parent_m: dict[str, str | None] = RELATIONS,
) -> dict[int, dict[int, list[ClassNetCacheProperty]]]:
    """
    Formats the class net cache.

    Arguments
    ---------
    class_net_cache : { int : { int : int } }
        A mapping of object IDs (keys) and secondary hash tables
        (values) containing stream ID-to-object ID pairs.
    classes : { int : str }
        A mapping of object IDs (keys) to their corresponding parent
        classes (values).
    object_parent_m : { str : str | None }
        A mapping of objects (keys) to their corresponding parent
        objects (values).

    """
    # Where our formatted entries will go
    formatted: dict[int, dict[int, int]] = {}

    # Iterate through the unformatted class net cache
    for idx, _cache in enumerate(class_net_cache):
        log.debug(f"idx: {idx}")

        # Get the class object where index==object_id
        class_object: FooterClass = classes[idx]
        log.debug(f"Class Object: {class_object.class_name}")

        # Get the class object's parent; Core.Object has no parent
        parent_name: str | None = object_parent_m.get(class_object.class_name)
        parent_obj: FooterClass | None = next(
            (x for x in classes if x.class_name == parent_name), None
        )
        log.debug(f"Parent: {parent_name}")
        log.debug(f"Parent: {parent_obj}")

        # Iteratively get parents (starting with `parent`) until a
        # corresponding entry is found in the formatted class net cache.
        # If parent is None (i.e. class_object is Core.Object), then
        # this loop won't run in the first place.
        # while parent_name:
        #     parent_object_id: int | None = parent_obj.object_id
        #     parent_properties: dict[int, int] | None = formatted.get(parent_object_id)
        #     log.debug(f"Parent ID: {parent_object_id}")
        #     log.debug(f"Parent Properties: {parent_properties}")
        #     if parent_properties is not None:
        #         # properties + parent_properties (no overwrite)
        #         final_properties: dict[int, list[ClassNetCacheProperty]] = {
        #             **parent_properties,
        #             **cache.properties,
        #         }
        #         break
        #     # `parent_properties` is None
        #     # set `parent` to the next parent
        #     parent = object_parent_m.get(parent)
        # else:  # No parent entry was found
        #     final_properties: list[ClassNetCacheProperty] = cache.properties

        # # Add new entry to `formatted`
        # formatted[idx] = final_properties

    return formatted
