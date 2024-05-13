import logging
from dataclasses import dataclass

from replay_parser.type import Bit_1, Bool_1, UInt_8, UInt_32, Vector3f

log = logging.getLogger(__name__)


@dataclass
class ActiveActor:
    active: Bool_1
    actor_id: UInt_32


@dataclass
class ActorBase:
    value: UInt_32
    unknown_002: Bit_1
    unknown_003: Bit_1


@dataclass
class AppliedDamage:
    id: UInt_8
    position: Vector3f
    damage_index: UInt_32
    total_damage: UInt_32


@dataclass
class CameraSettings:
    fov: float
    height: float
    angle: float
    distance: float
    stiffness: float
    swivel: float
    transition: float | None


@dataclass
class ClientLoadout:
    version: UInt_8
    body: UInt_32
    decal: UInt_32
    wheels: UInt_32
    rocket_trail: UInt_32
    antenna: UInt_32
    topper: UInt_32
    unknown_004: UInt_32
    unknown_005: UInt_32 | None
    engine_audio: UInt_32 | None
    trail: UInt_32 | None
    goal_explosion: UInt_32 | None
    banner: UInt_32 | None
    product_id: UInt_32 | None
    unknown_006: UInt_32 | None
    unknown_007: UInt_32 | None
    unknown_008: UInt_32 | None


@dataclass
class ClubColors:
    blue_flag: Bool_1
    blue_color: UInt_8
    orange_flag: Bool_1
    orange_color: UInt_8


@dataclass
class DamageState:
    tile_state: UInt_8
    damaged: Bool_1
    offender: UInt_32
    ball_position: Vector3f
    direct_hit: Bool_1
    immediate: Bool_1
