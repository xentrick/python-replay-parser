from dataclasses import dataclass
from enum import Enum, auto
from typing import Any, TypeAlias

Bool_1: TypeAlias = bool
Bool_8: TypeAlias = bool
UInt_64: TypeAlias = int


class SpawnTrajectory(Enum):
    NA = auto()
    Location = auto()
    LocationAndRotation = auto()


@dataclass
class GameField:
    name: str
    parent: str | None
    trajectory: SpawnTrajectory
    attr_type: Any


CLASSLIST = [
    GameField("Core.Object", None, SpawnTrajectory.NA, None),
    GameField("Engine.Actor", "Core.Object", SpawnTrajectory.Location, None),
    GameField("Engine.NavigationPoint", "Engine.Actor", SpawnTrajectory.Location, None),
    GameField("Engine.PlayerStart", "Engine.Actor", SpawnTrajectory.Location, None),
    GameField(
        "Engine.ReplicatedActor_ORS", "Engine.Actor", SpawnTrajectory.Location, None
    ),
    GameField(
        "TAGame.MaxTimeWarningData_TA",
        "Engine.ReplicatedActor_ORS",
        SpawnTrajectory.Location,
        UInt_64,
    ),
    GameField(
        "TAGame.Default__MaxTimeWarningData_TA",
        "TAGame.MaxTimeWarningData_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField("Engine.Info", "Engine.Actor", SpawnTrajectory.Location, None),
    GameField("Engine.ReplicationInfo", "Engine.Info", SpawnTrajectory.Location, None),
    GameField(
        "Engine.GameReplicationInfo",
        "Engine.ReplicationInfo",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "ProjectX.GRI_X", "Engine.GameReplicationInfo", SpawnTrajectory.Location, None
    ),
    GameField("TAGame.GRI_TA", "ProjectX.GRI_X", SpawnTrajectory.Location, None),
    GameField(
        "GameInfo_Basketball.GameInfo.GameInfo_Basketball:GameReplicationInfoArchetype",
        "TAGame.GRI_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "GameInfo_Breakout.GameInfo.GameInfo_Breakout:GameReplicationInfoArchetype",
        "TAGame.GRI_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Gameinfo_Hockey.GameInfo.Gameinfo_Hockey:GameReplicationInfoArchetype",
        "TAGame.GRI_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "GameInfo_Items.GameInfo.GameInfo_Items:GameReplicationInfoArchetype",
        "TAGame.GRI_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "GameInfo_Season.GameInfo.GameInfo_Season:GameReplicationInfoArchetype",
        "TAGame.GRI_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "GameInfo_Soccar.GameInfo.GameInfo_Soccar:GameReplicationInfoArchetype",
        "TAGame.GRI_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "GameInfo_Tutorial.GameInfo.GameInfo_Tutorial:GameReplicationInfoArchetype",
        "TAGame.GRI_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "GameInfo_GodBall.GameInfo.GameInfo_GodBall:GameReplicationInfoArchetype",
        "TAGame.GRI_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "GameInfo_FootBall.GameInfo.GameInfo_FootBall:GameReplicationInfoArchetype",
        "TAGame.GRI_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "GameInfo_KnockOut.KnockOut.GameInfo_KnockOut:GameReplicationInfoArchetype",
        "TAGame.GRI_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "GameInfo_FTE.GameInfo.GameInfo_FTE:GameReplicationInfoArchetype",
        "TAGame.GRI_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Engine.PlayerReplicationInfo",
        "Engine.ReplicationInfo",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "ProjectX.PRI_X", "Engine.PlayerReplicationInfo", SpawnTrajectory.Location, None
    ),
    GameField("TAGame.PRI_TA", "ProjectX.PRI_X", SpawnTrajectory.Location, None),
    GameField(
        "TAGame.PRI_Breakout_TA", "TAGame.PRI_TA", SpawnTrajectory.Location, None
    ),
    GameField(
        "TAGame.Default__PRI_Breakout_TA",
        "TAGame.PRI_Breakout_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.PRI_KnockOut_TA", "TAGame.PRI_TA", SpawnTrajectory.Location, None
    ),
    GameField(
        "TAGame.Default__PRI_KnockOut_TA",
        "TAGame.PRI_KnockOut_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.Default__PRI_TA", "TAGame.PRI_TA", SpawnTrajectory.Location, None
    ),
    GameField(
        "Engine.TeamInfo", "Engine.GameReplicationInfo", SpawnTrajectory.Location, None
    ),
    GameField("TAGame.Team_TA", "Engine.TeamInfo", SpawnTrajectory.Location, None),
    GameField(
        "TAGame.Team_Soccar_TA", "TAGame.Team_TA", SpawnTrajectory.Location, None
    ),
    GameField(
        "Archetypes.Teams.Team", "TAGame.Team_Soccar_TA", SpawnTrajectory.Location, None
    ),
    GameField(
        "ProjectX.NetModeReplicator_X",
        "Engine.ReplicationInfo",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "ProjectX.Default__NetModeReplicator_X",
        "ProjectX.NetModeReplicator_X",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.CarComponent_TA",
        "Engine.ReplicationInfo",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.CarComponent_AirActivate_TA",
        "TAGame.CarComponent_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.CarComponent_DoubleJump_TA",
        "TAGame.CarComponent_AirActivate_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.CarComponent_DoubleJump_KO_TA",
        "TAGame.CarComponent_DoubleJump_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.KnockOut.GameEvent_Knockout:CarArchetype.Jump",
        "TAGame.CarComponent_DoubleJump_KO_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.KnockOut.GameEvent_Knockout:CarArchetype.DoubleJump",
        "TAGame.CarComponent_DoubleJump_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.CarComponents.CarComponent_DoubleJump",
        "TAGame.CarComponent_DoubleJump_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.CarComponent_Boost_TA",
        "TAGame.CarComponent_AirActivate_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.CarComponent_Boost_KO_TA",
        "TAGame.CarComponent_Boost_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.KnockOut.GameEvent_Knockout:CarArchetype.Boost",
        "TAGame.CarComponent_Boost_KO_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.CarComponents.CarComponent_Boost",
        "TAGame.CarComponent_Boost_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.CarComponent_Dodge_TA",
        "TAGame.CarComponent_AirActivate_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.CarComponent_Dodge_KO_TA",
        "TAGame.CarComponent_Dodge_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.KnockOut.GameEvent_Knockout:CarArchetype.Dodge",
        "TAGame.CarComponent_Dodge_KO_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.CarComponents.CarComponent_Dodge",
        "TAGame.CarComponent_Dodge_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.CarComponent_TA",
        "Engine.ReplicationInfo",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.CarComponent_Jump_TA",
        "TAGame.CarComponent_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.CarComponents.CarComponent_Jump",
        "TAGame.CarComponent_Jump_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.CarComponent_FlipCar_TA",
        "TAGame.CarComponent_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.KnockOut.GameEvent_Knockout:CarArchetype.Flip",
        "TAGame.CarComponent_FlipCar_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.CarComponents.CarComponent_FlipCar",
        "TAGame.CarComponent_FlipCar_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.CarComponent_Torque_TA",
        "TAGame.CarComponent_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.KnockOut.GameEvent_Knockout:CarArchetype.Torque",
        "TAGame.CarComponent_Torque_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.SpecialPickup_TA",
        "TAGame.CarComponent_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.SpecialPickup_Targeted_TA",
        "TAGame.SpecialPickup_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.SpecialPickup_BallFreeze_TA",
        "TAGame.SpecialPickup_Targeted_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.SpecialPickups.SpecialPickup_BallFreeze",
        "TAGame.SpecialPickup_BallFreeze_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.SpecialPickup_Spring_TA",
        "TAGame.SpecialPickup_Targeted_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.SpecialPickup_BallCarSpring_TA",
        "TAGame.SpecialPickup_Spring_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.SpecialPickups.SpecialPickup_BallSpring",
        "TAGame.SpecialPickup_BallCarSpring_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.SpecialPickups.SpecialPickup_CarSpring",
        "TAGame.SpecialPickup_BallCarSpring_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.SpecialPickup_GrapplingHook_TA",
        "TAGame.SpecialPickup_Targeted_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.SpecialPickup_BallLasso_TA",
        "TAGame.SpecialPickup_GrapplingHook_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.SpecialPickup_Batarang_TA",
        "TAGame.SpecialPickup_BallLasso_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.SpecialPickups.SpecialPickup_Batarang",
        "TAGame.SpecialPickup_Batarang_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.SpecialPickups.SpecialPickup_BallLasso",
        "TAGame.SpecialPickup_BallLasso_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.SpecialPickups.SpecialPickup_BallGrapplingHook",
        "TAGame.SpecialPickup_GrapplingHook_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.SpecialPickup_BoostOverride_TA",
        "TAGame.SpecialPickup_Targeted_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.SpecialPickups.SpecialPickup_BoostOverride",
        "TAGame.SpecialPickup_BoostOverride_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.SpecialPickup_Swapper_TA",
        "TAGame.SpecialPickup_Targeted_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.SpecialPickups.SpecialPickup_Swapper",
        "TAGame.SpecialPickup_Swapper_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.SpecialPickup_Tornado_TA",
        "TAGame.SpecialPickup_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.SpecialPickups.SpecialPickup_Tornado",
        "TAGame.SpecialPickup_Tornado_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.SpecialPickup_HauntedBallBeam_TA",
        "TAGame.SpecialPickup_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.SpecialPickups.SpecialPickup_HauntedBallBeam",
        "TAGame.SpecialPickup_HauntedBallBeam_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.SpecialPickup_BallVelcro_TA",
        "TAGame.SpecialPickup_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.SpecialPickups.SpecialPickup_BallVelcro",
        "TAGame.SpecialPickup_BallVelcro_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.SpecialPickup_Rugby_TA",
        "TAGame.SpecialPickup_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.SpecialPickups.SpecialPickup_Rugby",
        "TAGame.SpecialPickup_Rugby_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.SpecialPickup_BallGravity_TA",
        "TAGame.SpecialPickup_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.SpecialPickups.SpecialPickup_GravityWell",
        "TAGame.SpecialPickup_BallGravity_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.SpecialPickup_HitForce_TA",
        "TAGame.SpecialPickup_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.SpecialPickups.SpecialPickup_StrongHit",
        "TAGame.SpecialPickup_HitForce_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.SpecialPickup_Football_TA",
        "TAGame.SpecialPickup_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.SpecialPickups.SpecialPickup_Football",
        "TAGame.SpecialPickup_Football_TA",
        SpawnTrajectory.Location,
        None,
    ),
    # Type from here
    GameField(
        "TAGame.PickupTimer_TA",
        "TAGame.CarComponent_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.Default__PickupTimer_TA",
        "TAGame.PickupTimer_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.CrowdManager_TA",
        "Engine.ReplicationInfo",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TheWorld:PersistentLevel.CrowdManager_TA",
        "TAGame.CrowdManager_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.CrowdActor_TA", "Engine.ReplicationInfo", SpawnTrajectory.Location, None
    ),
    GameField(
        "TheWorld:PersistentLevel.CrowdActor_TA",
        "TAGame.CrowdActor_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.CameraSettingsActor_TA",
        "Engine.ReplicationInfo",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.Default__CameraSettingsActor_TA",
        "TAGame.CameraSettingsActor_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.VehiclePickup_TA",
        "Engine.ReplicationInfo",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.VehiclePickup_Boost_TA",
        "TAGame.VehiclePickup_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TheWorld:PersistentLevel.VehiclePickup_Boost_TA",
        "TAGame.VehiclePickup_Boost_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.VehiclePickup_Item_TA",
        "TAGame.VehiclePickup_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.GameEvent_TA", "Engine.ReplicationInfo", SpawnTrajectory.Location, None
    ),
    GameField(
        "TAGame.GameEvent_Team_TA",
        "TAGame.GameEvent_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.GameEvent_Soccar_TA",
        "TAGame.GameEvent_Team_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.GameEvent_KnockOut_TA",
        "TAGame.GameEvent_Soccar_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.KnockOut.GameEvent_Knockout",
        "TAGame.GameEvent_KnockOut_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.GameEvent_FTE_TA",
        "TAGame.GameEvent_Soccar_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.GameEvent.GameEvent_FTE_Part1_Prime",
        "TAGame.GameEvent_FTE_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.GameEvent_Breakout_TA",
        "TAGame.GameEvent_Soccar_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.GameEvent_Football_TA",
        "TAGame.GameEvent_Soccar_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "GameInfo_FootBall.GameInfo.GameInfo_FootBall:Archetype",
        "TAGame.GameEvent_Football_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.GameEvent_GodBall_TA",
        "TAGame.GameEvent_Soccar_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "GameInfo_GodBall.GameInfo.GameInfo_GodBall:Archetype",
        "TAGame.GameEvent_GodBall_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.GameEvent_Season_TA",
        "TAGame.GameEvent_Soccar_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.GameEvent.GameEvent_Season",
        "TAGame.GameEvent_Season_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.GameEvent_SoccarPrivate_TA",
        "TAGame.GameEvent_Soccar_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.GameEvent_SoccarSplitscreen_TA",
        "TAGame.GameEvent_SoccarPrivate_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.GameEvent.GameEvent_BasketballSplitscreen",
        "TAGame.GameEvent_SoccarSplitscreen_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.GameEvent.GameEvent_HockeySplitscreen",
        "TAGame.GameEvent_SoccarSplitscreen_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.GameEvent.GameEvent_SoccarSplitscreen",
        "TAGame.GameEvent_SoccarSplitscreen_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.GameEvent.GameEvent_BasketballPrivate",
        "TAGame.GameEvent_SoccarPrivate_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.GameEvent.GameEvent_HockeyPrivate",
        "TAGame.GameEvent_SoccarPrivate_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.GameEvent.GameEvent_SoccarPrivate",
        "TAGame.GameEvent_SoccarPrivate_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.GameEvent_Tutorial_TA",
        "TAGame.GameEvent_Soccar_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.GameEvent_Tutorial_Goalie_TA",
        "TAGame.GameEvent_Tutorial_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.GameEvent_Tutorial_Striker_TA",
        "TAGame.GameEvent_Tutorial_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "GameInfo_Tutorial.GameEvent.GameEvent_Tutorial_Aerial",
        "TAGame.GameEvent_Tutorial_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.GameEvent_GameEditor_TA",
        "TAGame.GameEvent_Soccar_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.GameEvent_TrainingEditor_TA",
        "TAGame.GameEvent_GameEditor_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.GameEvent.GameEvent_Basketball",
        "TAGame.GameEvent_Soccar_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.GameEvent.GameEvent_Breakout",
        "TAGame.GameEvent_Soccar_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.GameEvent.GameEvent_Hockey",
        "TAGame.GameEvent_Soccar_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.GameEvent.GameEvent_Items",
        "TAGame.GameEvent_Soccar_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.GameEvent.GameEvent_Soccar",
        "TAGame.GameEvent_Soccar_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.GameEvent.GameEvent_SoccarLan",
        "TAGame.GameEvent_Soccar_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField("Engine.WorldInfo", "Engine.Info", SpawnTrajectory.Location, None),
    GameField("TAGame.VoteActor_TA", "Engine.Info", SpawnTrajectory.Location, None),
    GameField(
        "TAGame.Default__VoteActor_TA",
        "TAGame.VoteActor_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField("Engine.Pawn", "Engine.Actor", SpawnTrajectory.Location, None),
    GameField("ProjectX.Pawn_X", "Engine.Pawn", SpawnTrajectory.Location, None),
    GameField("TAGame.RBActor_TA", "ProjectX.Pawn_X", SpawnTrajectory.Location, None),
    GameField("TAGame.Ball_TA", "TAGame.RBActor_TA", SpawnTrajectory.Location, None),
    GameField(
        "TAGame.Ball_Trajectory_TA", "TAGame.Ball_TA", SpawnTrajectory.Location, None
    ),
    GameField(
        "TAGame.Ball_Breakout_TA",
        "Archetypes.Ball.Ball_Breakout",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.Ball.Ball_Breakout",
        "TAGame.Ball_Breakout_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField("TAGame.Ball_God_TA", "TAGame.Ball_TA", SpawnTrajectory.Location, None),
    GameField(
        "Archetypes.Ball.Ball_God", "TAGame.Ball_God_TA", SpawnTrajectory.Location, None
    ),
    GameField(
        "TAGame.Ball_Haunted_TA", "TAGame.Ball_TA", SpawnTrajectory.Location, None
    ),
    GameField(
        "Archetypes.Ball.Ball_Haunted",
        "TAGame.Ball_Haunted_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.Ball.Ball_BasketBall_Mutator",
        "TAGame.Ball_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.Ball.Ball_Basketball",
        "TAGame.Ball_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.Ball.Ball_Beachball",
        "TAGame.Ball_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.Ball.Ball_Default", "TAGame.Ball_TA", SpawnTrajectory.Location, None
    ),
    GameField(
        "Archetypes.Ball.Ball_Trajectory",
        "TAGame.Ball_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.Ball.Ball_Puck", "TAGame.Ball_TA", SpawnTrajectory.Location, None
    ),
    GameField(
        "Archetypes.Ball.Ball_Anniversary",
        "TAGame.Ball_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.Ball.CubeBall", "TAGame.Ball_TA", SpawnTrajectory.Location, None
    ),
    GameField(
        "Archetypes.Ball.Ball_Training",
        "TAGame.Ball_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.Ball.Ball_Football",
        "TAGame.Ball_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField("TAGame.Vehicle_TA", "TAGame.RBActor_TA", SpawnTrajectory.Location, None),
    GameField("TAGame.Car_TA", "TAGame.Vehicle_TA", SpawnTrajectory.Location, None),
    GameField(
        "Archetypes.GameEvent.GameEvent_Season:CarArchetype",
        "",
        SpawnTrajectory.Location,
        None,
    ),
    GameField("TAGame.Car_Season_TA", "TAGame.Car_TA", SpawnTrajectory.Location, None),
    GameField(
        "TAGame.Car_Freeplay_TA", "TAGame.Car_TA", SpawnTrajectory.Location, None
    ),
    GameField(
        "TAGame.Car_KnockOut_TA", "TAGame.Car_TA", SpawnTrajectory.Location, None
    ),
    GameField(
        "Archetypes.KnockOut.GameEvent_Knockout:CarArchetype",
        "TAGame.Car_KnockOut_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "Archetypes.Car.Car_Default", "TAGame.Car_TA", SpawnTrajectory.Location, None
    ),
    GameField(
        "Archetypes.Car.Car_PostGameLobby",
        "TAGame.Car_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.Default__Car_TA", "TAGame.Car_TA", SpawnTrajectory.Location, None
    ),
    GameField(
        "TAGame.GameEditor_Pawn_TA", "ProjectX.Pawn_X", SpawnTrajectory.Location, None
    ),
    GameField("Engine.DynamicSMActor", "Engine.Actor", SpawnTrajectory.Location, None),
    GameField("Engine.KActor", "Engine.DynamicSMActor", SpawnTrajectory.Location, None),
    GameField(
        "TAGame.BreakOutActor_Platform_TA",
        "Engine.Actor",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TheWorld:PersistentLevel.BreakOutActor_Platform_TA",
        "TAGame.BreakOutActor_Platform_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.InMapScoreboard_TA", "Engine.Actor", SpawnTrajectory.Location, None
    ),
    GameField(
        "TheWorld:PersistentLevel.InMapScoreboard_TA",
        "TAGame.InMapScoreboard_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.HauntedBallTrapTrigger_TA",
        "Engine.Actor",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TheWorld:PersistentLevel.HauntedBallTrapTrigger_TA",
        "TAGame.HauntedBallTrapTrigger_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.RumblePickups_TA", "Engine.Actor", SpawnTrajectory.Location, None
    ),
    GameField(
        "TAGame.Default__RumblePickups_TA",
        "TAGame.RumblePickups_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField("TAGame.Cannon_TA", "Engine.Actor", SpawnTrajectory.Location, None),
    GameField(
        "Archetypes.Tutorial.Cannon", "TAGame.Cannon_TA", SpawnTrajectory.Location, None
    ),
    GameField("TAGame.Stunlock_TA", "Engine.Actor", SpawnTrajectory.Location, None),
    GameField(
        "Archetypes.KnockOut.GameEvent_Knockout:CarArchetype.StunlockArchetype",
        "TAGame.Stunlock_TA",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TAGame.PlayerStart_Platform_TA",
        "Engine.Actor ",
        SpawnTrajectory.Location,
        None,
    ),
    GameField(
        "TheWorld:PersistentLevel.PlayerStart_Platform_TA",
        "TAGame.PlayerStart_Platform_TA",
        SpawnTrajectory.Location,
        None,
    ),
]


RELATIONS = {
    "Core.Object": None,
    "Engine.Actor": "Core.Object",
    "Engine.NavigationPoint": "Engine.Actor",
    "Engine.PlayerStart": "Engine.Actor",
    "Engine.ReplicatedActor_ORS": "Engine.Actor",
    "TAGame.MaxTimeWarningData_TA": "Engine.ReplicatedActor_ORS",
    "TAGame.Default__MaxTimeWarningData_TA": "TAGame.MaxTimeWarningData_TA",
    "Engine.Info": "Engine.Actor",
    "Engine.ReplicationInfo": "Engine.Info",
    "Engine.GameReplicationInfo": "Engine.ReplicationInfo",
    "ProjectX.GRI_X": "Engine.GameReplicationInfo",
    "TAGame.GRI_TA": "ProjectX.GRI_X",
    "GameInfo_Basketball.GameInfo.GameInfo_Basketball:GameReplicationInfoArchetype": "TAGame.GRI_TA",
    "GameInfo_Breakout.GameInfo.GameInfo_Breakout:GameReplicationInfoArchetype": "TAGame.GRI_TA",
    "Gameinfo_Hockey.GameInfo.Gameinfo_Hockey:GameReplicationInfoArchetype": "TAGame.GRI_TA",
    "GameInfo_Items.GameInfo.GameInfo_Items:GameReplicationInfoArchetype": "TAGame.GRI_TA",
    "GameInfo_Season.GameInfo.GameInfo_Season:GameReplicationInfoArchetype": "TAGame.GRI_TA",
    "GameInfo_Soccar.GameInfo.GameInfo_Soccar:GameReplicationInfoArchetype": "TAGame.GRI_TA",
    "GameInfo_Tutorial.GameInfo.GameInfo_Tutorial:GameReplicationInfoArchetype": "TAGame.GRI_TA",
    "GameInfo_GodBall.GameInfo.GameInfo_GodBall:GameReplicationInfoArchetype": "TAGame.GRI_TA",
    "GameInfo_FootBall.GameInfo.GameInfo_FootBall:GameReplicationInfoArchetype": "TAGame.GRI_TA",
    "GameInfo_KnockOut.KnockOut.GameInfo_KnockOut:GameReplicationInfoArchetype": "TAGame.GRI_TA",
    "GameInfo_FTE.GameInfo.GameInfo_FTE:GameReplicationInfoArchetype": "TAGame.GRI_TA",
    "Engine.PlayerReplicationInfo": "Engine.ReplicationInfo",
    "ProjectX.PRI_X": "Engine.PlayerReplicationInfo",
    "TAGame.PRI_TA": "ProjectX.PRI_X",
    "TAGame.PRI_Breakout_TA": "TAGame.PRI_TA",
    "TAGame.Default__PRI_Breakout_TA": "TAGame.PRI_Breakout_TA",
    "TAGame.PRI_KnockOut_TA": "TAGame.PRI_TA",
    "TAGame.Default__PRI_KnockOut_TA": "TAGame.PRI_KnockOut_TA",
    "TAGame.Default__PRI_TA": "TAGame.PRI_TA",
    "Engine.TeamInfo": "Engine.GameReplicationInfo",
    "TAGame.Team_TA": "Engine.TeamInfo",
    "TAGame.Team_Soccar_TA": "TAGame.Team_TA",
    "Archetypes.Teams.Team": "TAGame.Team_Soccar_TA",
    "ProjectX.NetModeReplicator_X": "Engine.ReplicationInfo",
    "ProjectX.Default__NetModeReplicator_X": "ProjectX.NetModeReplicator_X",
    "TAGame.CarComponent_TA": "Engine.ReplicationInfo",
    "TAGame.CarComponent_AirActivate_TA": "TAGame.CarComponent_TA",
    "TAGame.CarComponent_DoubleJump_TA": "TAGame.CarComponent_AirActivate_TA",
    "TAGame.CarComponent_DoubleJump_KO_TA": "TAGame.CarComponent_DoubleJump_TA",
    "Archetypes.KnockOut.GameEvent_Knockout:CarArchetype.Jump": "TAGame.CarComponent_DoubleJump_KO_TA",
    "Archetypes.KnockOut.GameEvent_Knockout:CarArchetype.DoubleJump": "TAGame.CarComponent_DoubleJump_TA",
    "Archetypes.CarComponents.CarComponent_DoubleJump": "TAGame.CarComponent_DoubleJump_TA",
    "TAGame.CarComponent_Boost_TA": "TAGame.CarComponent_AirActivate_TA",
    "TAGame.CarComponent_Boost_KO_TA": "TAGame.CarComponent_Boost_TA",
    "Archetypes.KnockOut.GameEvent_Knockout:CarArchetype.Boost": "TAGame.CarComponent_Boost_KO_TA",
    "Archetypes.CarComponents.CarComponent_Boost": "TAGame.CarComponent_Boost_TA",
    "TAGame.CarComponent_Dodge_TA": "TAGame.CarComponent_AirActivate_TA",
    "TAGame.CarComponent_Dodge_KO_TA": "TAGame.CarComponent_Dodge_TA",
    "Archetypes.KnockOut.GameEvent_Knockout:CarArchetype.Dodge": "TAGame.CarComponent_Dodge_KO_TA",
    "Archetypes.CarComponents.CarComponent_Dodge": "TAGame.CarComponent_Dodge_TA",
    "TAGame.CarComponent_TA": "Engine.ReplicationInfo",
    "TAGame.CarComponent_Jump_TA": "TAGame.CarComponent_TA",
    "Archetypes.CarComponents.CarComponent_Jump": "TAGame.CarComponent_Jump_TA",
    "TAGame.CarComponent_FlipCar_TA": "TAGame.CarComponent_TA",
    "Archetypes.KnockOut.GameEvent_Knockout:CarArchetype.Flip": "TAGame.CarComponent_FlipCar_TA",
    "Archetypes.CarComponents.CarComponent_FlipCar": "TAGame.CarComponent_FlipCar_TA",
    "TAGame.CarComponent_Torque_TA": "TAGame.CarComponent_TA",
    "Archetypes.KnockOut.GameEvent_Knockout:CarArchetype.Torque": "TAGame.CarComponent_Torque_TA",
    "TAGame.SpecialPickup_TA": "TAGame.CarComponent_TA",
    "TAGame.SpecialPickup_Targeted_TA": "TAGame.SpecialPickup_TA",
    "TAGame.SpecialPickup_BallFreeze_TA": "TAGame.SpecialPickup_Targeted_TA",
    "Archetypes.SpecialPickups.SpecialPickup_BallFreeze": "TAGame.SpecialPickup_BallFreeze_TA",
    "TAGame.SpecialPickup_Spring_TA": "TAGame.SpecialPickup_Targeted_TA",
    "TAGame.SpecialPickup_BallCarSpring_TA": "TAGame.SpecialPickup_Spring_TA",
    "Archetypes.SpecialPickups.SpecialPickup_BallSpring": "TAGame.SpecialPickup_BallCarSpring_TA",
    "Archetypes.SpecialPickups.SpecialPickup_CarSpring": "TAGame.SpecialPickup_BallCarSpring_TA",
    "TAGame.SpecialPickup_GrapplingHook_TA": "TAGame.SpecialPickup_Targeted_TA",
    "TAGame.SpecialPickup_BallLasso_TA": "TAGame.SpecialPickup_GrapplingHook_TA",
    "TAGame.SpecialPickup_Batarang_TA": "TAGame.SpecialPickup_BallLasso_TA",
    "Archetypes.SpecialPickups.SpecialPickup_Batarang": "TAGame.SpecialPickup_Batarang_TA",
    "Archetypes.SpecialPickups.SpecialPickup_BallLasso": "TAGame.SpecialPickup_BallLasso_TA",
    "Archetypes.SpecialPickups.SpecialPickup_BallGrapplingHook": "TAGame.SpecialPickup_GrapplingHook_TA",
    "TAGame.SpecialPickup_BoostOverride_TA": "TAGame.SpecialPickup_Targeted_TA",
    "Archetypes.SpecialPickups.SpecialPickup_BoostOverride": "TAGame.SpecialPickup_BoostOverride_TA",
    "TAGame.SpecialPickup_Swapper_TA": "TAGame.SpecialPickup_Targeted_TA",
    "Archetypes.SpecialPickups.SpecialPickup_Swapper": "TAGame.SpecialPickup_Swapper_TA",
    "TAGame.SpecialPickup_Tornado_TA": "TAGame.SpecialPickup_TA",
    "Archetypes.SpecialPickups.SpecialPickup_Tornado": "TAGame.SpecialPickup_Tornado_TA",
    "TAGame.SpecialPickup_HauntedBallBeam_TA": "TAGame.SpecialPickup_TA",
    "Archetypes.SpecialPickups.SpecialPickup_HauntedBallBeam": "TAGame.SpecialPickup_HauntedBallBeam_TA",
    "TAGame.SpecialPickup_BallVelcro_TA": "TAGame.SpecialPickup_TA",
    "Archetypes.SpecialPickups.SpecialPickup_BallVelcro": "TAGame.SpecialPickup_BallVelcro_TA",
    "TAGame.SpecialPickup_Rugby_TA": "TAGame.SpecialPickup_TA",
    "Archetypes.SpecialPickups.SpecialPickup_Rugby": "TAGame.SpecialPickup_Rugby_TA",
    "TAGame.SpecialPickup_BallGravity_TA": "TAGame.SpecialPickup_TA",
    "Archetypes.SpecialPickups.SpecialPickup_GravityWell": "TAGame.SpecialPickup_BallGravity_TA",
    "TAGame.SpecialPickup_HitForce_TA": "TAGame.SpecialPickup_TA",
    "Archetypes.SpecialPickups.SpecialPickup_StrongHit": "TAGame.SpecialPickup_HitForce_TA",
    "TAGame.SpecialPickup_Football_TA": "TAGame.SpecialPickup_TA",
    "Archetypes.SpecialPickups.SpecialPickup_Football": "TAGame.SpecialPickup_Football_TA",
    "TAGame.PickupTimer_TA": "TAGame.CarComponent_TA",
    "TAGame.Default__PickupTimer_TA": "TAGame.PickupTimer_TA",
    "TAGame.CrowdManager_TA": "Engine.ReplicationInfo",
    "TheWorld:PersistentLevel.CrowdManager_TA": "TAGame.CrowdManager_TA",
    "TAGame.CrowdActor_TA": "Engine.ReplicationInfo",
    "TheWorld:PersistentLevel.CrowdActor_TA": "TAGame.CrowdActor_TA",
    "TAGame.CameraSettingsActor_TA": "Engine.ReplicationInfo",
    "TAGame.Default__CameraSettingsActor_TA": "TAGame.CameraSettingsActor_TA",
    "TAGame.VehiclePickup_TA": "Engine.ReplicationInfo",
    "TAGame.VehiclePickup_Boost_TA": "TAGame.VehiclePickup_TA",
    "TheWorld:PersistentLevel.VehiclePickup_Boost_TA": "TAGame.VehiclePickup_Boost_TA",
    "TAGame.VehiclePickup_Item_TA": "TAGame.VehiclePickup_TA",
    "TAGame.GameEvent_TA": "Engine.ReplicationInfo",
    "TAGame.GameEvent_Team_TA": "TAGame.GameEvent_TA",
    "TAGame.GameEvent_Soccar_TA": "TAGame.GameEvent_Team_TA",
    "TAGame.GameEvent_KnockOut_TA": "TAGame.GameEvent_Soccar_TA",
    "Archetypes.KnockOut.GameEvent_Knockout": "TAGame.GameEvent_KnockOut_TA",
    "TAGame.GameEvent_FTE_TA": "TAGame.GameEvent_Soccar_TA",
    "Archetypes.GameEvent.GameEvent_FTE_Part1_Prime": "TAGame.GameEvent_FTE_TA",
    "TAGame.GameEvent_Breakout_TA": "TAGame.GameEvent_Soccar_TA",
    "TAGame.GameEvent_Football_TA": "TAGame.GameEvent_Soccar_TA",
    "GameInfo_FootBall.GameInfo.GameInfo_FootBall:Archetype": "TAGame.GameEvent_Football_TA",
    "TAGame.GameEvent_GodBall_TA": "TAGame.GameEvent_Soccar_TA",
    "GameInfo_GodBall.GameInfo.GameInfo_GodBall:Archetype": "TAGame.GameEvent_GodBall_TA",
    "TAGame.GameEvent_Season_TA": "TAGame.GameEvent_Soccar_TA",
    "Archetypes.GameEvent.GameEvent_Season": "TAGame.GameEvent_Season_TA",
    "TAGame.GameEvent_SoccarPrivate_TA": "TAGame.GameEvent_Soccar_TA",
    "TAGame.GameEvent_SoccarSplitscreen_TA": "TAGame.GameEvent_SoccarPrivate_TA",
    "Archetypes.GameEvent.GameEvent_BasketballSplitscreen": "TAGame.GameEvent_SoccarSplitscreen_TA",
    "Archetypes.GameEvent.GameEvent_HockeySplitscreen": "TAGame.GameEvent_SoccarSplitscreen_TA",
    "Archetypes.GameEvent.GameEvent_SoccarSplitscreen": "TAGame.GameEvent_SoccarSplitscreen_TA",
    "Archetypes.GameEvent.GameEvent_BasketballPrivate": "TAGame.GameEvent_SoccarPrivate_TA",
    "Archetypes.GameEvent.GameEvent_HockeyPrivate": "TAGame.GameEvent_SoccarPrivate_TA",
    "Archetypes.GameEvent.GameEvent_SoccarPrivate": "TAGame.GameEvent_SoccarPrivate_TA",
    "TAGame.GameEvent_Tutorial_TA": "TAGame.GameEvent_Soccar_TA",
    "TAGame.GameEvent_Tutorial_Goalie_TA": "TAGame.GameEvent_Tutorial_TA",
    "TAGame.GameEvent_Tutorial_Striker_TA": "TAGame.GameEvent_Tutorial_TA",
    "GameInfo_Tutorial.GameEvent.GameEvent_Tutorial_Aerial": "TAGame.GameEvent_Tutorial_TA",
    "TAGame.GameEvent_GameEditor_TA": "TAGame.GameEvent_Soccar_TA",
    "TAGame.GameEvent_TrainingEditor_TA": "TAGame.GameEvent_GameEditor_TA",
    "Archetypes.GameEvent.GameEvent_Basketball": "TAGame.GameEvent_Soccar_TA",
    "Archetypes.GameEvent.GameEvent_Breakout": "TAGame.GameEvent_Soccar_TA",
    "Archetypes.GameEvent.GameEvent_Hockey": "TAGame.GameEvent_Soccar_TA",
    "Archetypes.GameEvent.GameEvent_Items": "TAGame.GameEvent_Soccar_TA",
    "Archetypes.GameEvent.GameEvent_Soccar": "TAGame.GameEvent_Soccar_TA",
    "Archetypes.GameEvent.GameEvent_SoccarLan": "TAGame.GameEvent_Soccar_TA",
    "Engine.WorldInfo": "Engine.Info",
    "TAGame.VoteActor_TA": "Engine.Info",
    "TAGame.Default__VoteActor_TA": "TAGame.VoteActor_TA",
    "Engine.Pawn": "Engine.Actor",
    "ProjectX.Pawn_X": "Engine.Pawn",
    "TAGame.RBActor_TA": "ProjectX.Pawn_X",
    "TAGame.Ball_TA": "TAGame.RBActor_TA",
    "TAGame.Ball_Trajectory_TA": "TAGame.Ball_TA",
    "TAGame.Ball_Breakout_TA": "Archetypes.Ball.Ball_Breakout",
    "Archetypes.Ball.Ball_Breakout": "TAGame.Ball_Breakout_TA",
    "TAGame.Ball_God_TA": "TAGame.Ball_TA",
    "Archetypes.Ball.Ball_God": "TAGame.Ball_God_TA",
    "TAGame.Ball_Haunted_TA": "TAGame.Ball_TA",
    "Archetypes.Ball.Ball_Haunted": "TAGame.Ball_Haunted_TA",
    "Archetypes.Ball.Ball_BasketBall_Mutator": "TAGame.Ball_TA",
    "Archetypes.Ball.Ball_Basketball": "TAGame.Ball_TA",
    "Archetypes.Ball.Ball_Beachball": "TAGame.Ball_TA",
    "Archetypes.Ball.Ball_Default": "TAGame.Ball_TA",
    "Archetypes.Ball.Ball_Trajectory": "TAGame.Ball_TA",
    "Archetypes.Ball.Ball_Puck": "TAGame.Ball_TA",
    "Archetypes.Ball.Ball_Anniversary": "TAGame.Ball_TA",
    "Archetypes.Ball.CubeBall": "TAGame.Ball_TA",
    "Archetypes.Ball.Ball_Training": "TAGame.Ball_TA",
    "Archetypes.Ball.Ball_Football": "TAGame.Ball_TA",
    "TAGame.Vehicle_TA": "TAGame.RBActor_TA",
    "TAGame.Car_TA": "TAGame.Vehicle_TA",
    "Archetypes.GameEvent.GameEvent_Season:CarArchetype": "",
    "TAGame.Car_Season_TA": "TAGame.Car_TA",
    "TAGame.Car_Freeplay_TA": "TAGame.Car_TA",
    "TAGame.Car_KnockOut_TA": "TAGame.Car_TA",
    "Archetypes.KnockOut.GameEvent_Knockout:CarArchetype": "TAGame.Car_KnockOut_TA",
    "Archetypes.Car.Car_Default": "TAGame.Car_TA",
    "Archetypes.Car.Car_PostGameLobby": "TAGame.Car_TA",
    "TAGame.Default__Car_TA": "TAGame.Car_TA",
    "TAGame.GameEditor_Pawn_TA": "ProjectX.Pawn_X",
    "Engine.DynamicSMActor": "Engine.Actor",
    "Engine.KActor": "Engine.DynamicSMActor",
    "TAGame.BreakOutActor_Platform_TA": "Engine.Actor",
    "TheWorld:PersistentLevel.BreakOutActor_Platform_TA": "TAGame.BreakOutActor_Platform_TA",
    "TAGame.InMapScoreboard_TA": "Engine.Actor",
    "TheWorld:PersistentLevel.InMapScoreboard_TA": "TAGame.InMapScoreboard_TA",
    "TAGame.HauntedBallTrapTrigger_TA": "Engine.Actor",
    "TheWorld:PersistentLevel.HauntedBallTrapTrigger_TA": "TAGame.HauntedBallTrapTrigger_TA",
    "TAGame.RumblePickups_TA": "Engine.Actor",
    "TAGame.Default__RumblePickups_TA": "TAGame.RumblePickups_TA",
    "TAGame.Cannon_TA": "Engine.Actor",
    "Archetypes.Tutorial.Cannon": "TAGame.Cannon_TA",
    "TAGame.Stunlock_TA": "Engine.Actor",
    "Archetypes.KnockOut.GameEvent_Knockout:CarArchetype.StunlockArchetype": "TAGame.Stunlock_TA",
    "TAGame.PlayerStart_Platform_TA": "Engine.Actor ",
    "TheWorld:PersistentLevel.PlayerStart_Platform_TA": "TAGame.PlayerStart_Platform_TA",
}


# CLASSMAP = {
# # Core.Object
#     "Engine.Actor": "Core.Object",
#     "Engine.NavigationPoint": "Engine.Actor",
#     "Engine.PlayerStart": "Engine.Actor",

#     "Engine.ReplicatedActor_ORS": "Engine.Actor",
#     "TAGame.MaxTimeWarningData_TA": "Engine.ReplicatedActor_ORS",
#     "TAGame.Default__MaxTimeWarningData_TA": "TAGame.MaxTimeWarningData_TA",

#     "Engine.Info": "Engine.Actor",
#     "Engine.ReplicationInfo": "Engine.Info",

#     "Engine.GameReplicationInfo": "Engine.ReplicationInfo",
#     "ProjectX.GRI_X": "Engine.GameReplicationInfo",
#     "TAGame.GRI_TA": "ProjectX.GRI_X",
#     "GameInfo_Basketball.GameInfo.GameInfo_Basketball:GameReplicationInfoArchetype": "TAGame.GRI_TA",
#     "GameInfo_Breakout.GameInfo.GameInfo_Breakout:GameReplicationInfoArchetype": "TAGame.GRI_TA",
#     "Gameinfo_Hockey.GameInfo.Gameinfo_Hockey:GameReplicationInfoArchetype": "TAGame.GRI_TA",
#     "GameInfo_Items.GameInfo.GameInfo_Items:GameReplicationInfoArchetype": "TAGame.GRI_TA",
#     "GameInfo_Season.GameInfo.GameInfo_Season:GameReplicationInfoArchetype": "TAGame.GRI_TA",
#     "GameInfo_Soccar.GameInfo.GameInfo_Soccar:GameReplicationInfoArchetype": "TAGame.GRI_TA",
#     "GameInfo_Tutorial.GameInfo.GameInfo_Tutorial:GameReplicationInfoArchetype": "TAGame.GRI_TA",
#     "GameInfo_GodBall.GameInfo.GameInfo_GodBall:GameReplicationInfoArchetype": "TAGame.GRI_TA",
#     "GameInfo_FootBall.GameInfo.GameInfo_FootBall:GameReplicationInfoArchetype": "TAGame.GRI_TA",
#     "GameInfo_KnockOut.KnockOut.GameInfo_KnockOut:GameReplicationInfoArchetype": "TAGame.GRI_TA",
#     "GameInfo_FTE.GameInfo.GameInfo_FTE:GameReplicationInfoArchetype": "TAGame.GRI_TA",

#     "Engine.PlayerReplicationInfo": "Engine.GameReplicationInfo",
#     "ProjectX.PRI_X": "Engine.PlayerReplicationInfo",
#     "TAGame.PRI_TA": "ProjectX.PRI_X",
#     "TAGame.PRI_Breakout_TA": "TAGame.PRI_TA",
#     "TAGame.Default__PRI_Breakout_TA": "TAGame.PRI_Breakout_TA",
#     "TAGame.PRI_KnockOut_TA": "TAGame.PRI_TA",
#     "TAGame.Default__PRI_KnockOut_TA": "TAGame.PRI_KnockOut_TA",
#     "TAGame.Default__PRI_TA": "TAGame.PRI_TA",

#     Engine.TeamInfo
#     └── TAGame.Team_TA
#         └── TAGame.Team_Soccar_TA
#             └── Archetypes.Teams.Team
#     ProjectX.NetModeReplicator_X
#     └── ProjectX.Default__NetModeReplicator_X
#     TAGame.CarComponent_TA
#     ├── TAGame.CarComponent_AirActivate_TA
#     │   ├── TAGame.CarComponent_DoubleJump_TA
#     │   │   ├── TAGame.CarComponent_DoubleJump_KO_TA
#     │   │   │   └── Archetypes.KnockOut.GameEvent_Knockout:CarArchetype.Jump
#     │   │   ├── Archetypes.KnockOut.GameEvent_Knockout:CarArchetype.DoubleJump
#     │   │   └── Archetypes.CarComponents.CarComponent_DoubleJump
#     │   ├── TAGame.CarComponent_Boost_TA
#     │   │   ├── TAGame.CarComponent_Boost_KO_TA
#     │   │   │   └── Archetypes.KnockOut.GameEvent_Knockout:CarArchetype.Boost
#     │   │   └── Archetypes.CarComponents.CarComponent_Boost
#     │   └── TAGame.CarComponent_Dodge_TA
#     │       ├── TAGame.CarComponent_Dodge_KO_TA
#     │       │   └── Archetypes.KnockOut.GameEvent_Knockout:CarArchetype.Dodge
#     │       └── Archetypes.CarComponents.CarComponent_Dodge
#     ├── TAGame.CarComponent_Jump_TA
#     │   └── Archetypes.CarComponents.CarComponent_Jump
#     ├── TAGame.CarComponent_FlipCar_TA
#     │   ├── Archetypes.KnockOut.GameEvent_Knockout:CarArchetype.Flip
#     │   └── Archetypes.CarComponents.CarComponent_FlipCar
#     ├── TAGame.CarComponent_Torque_TA
#     │   └── Archetypes.KnockOut.GameEvent_Knockout:CarArchetype.Torque
#     ├── TAGame.SpecialPickup_TA
#     │   ├── TAGame.SpecialPickup_Targeted_TA
#     │   │   ├── TAGame.SpecialPickup_BallFreeze_TA
#     │   │   │   └── Archetypes.SpecialPickups.SpecialPickup_BallFreeze
#     │   │   ├── TAGame.SpecialPickup_Spring_TA
#     │   │   │   └── TAGame.SpecialPickup_BallCarSpring_TA
#     │   │   │       ├── Archetypes.SpecialPickups.SpecialPickup_BallSpring
#     │   │   │       └── Archetypes.SpecialPickups.SpecialPickup_CarSpring
#     │   │   ├── TAGame.SpecialPickup_GrapplingHook_TA
#     │   │   │   ├── TAGame.SpecialPickup_BallLasso_TA
#     │   │   │   │   ├── TAGame.SpecialPickup_Batarang_TA
#     │   │   │   │   │   └── Archetypes.SpecialPickups.SpecialPickup_Batarang
#     │   │   │   │   └── Archetypes.SpecialPickups.SpecialPickup_BallLasso
#     │   │   │   └── Archetypes.SpecialPickups.SpecialPickup_BallGrapplingHook
#     │   │   ├── TAGame.SpecialPickup_BoostOverride_TA
#     │   │   │   └── Archetypes.SpecialPickups.SpecialPickup_BoostOverride
#     │   │   └── TAGame.SpecialPickup_Swapper_TA
#     │   │       └── Archetypes.SpecialPickups.SpecialPickup_Swapper
#     │   ├── TAGame.SpecialPickup_Tornado_TA
#     │   │   └── Archetypes.SpecialPickups.SpecialPickup_Tornado
#     │   ├── TAGame.SpecialPickup_HauntedBallBeam_TA
#     │   │   └── Archetypes.SpecialPickups.SpecialPickup_HauntedBallBeam
#     │   ├── TAGame.SpecialPickup_BallVelcro_TA
#     │   │   └── Archetypes.SpecialPickups.SpecialPickup_BallVelcro
#     │   ├── TAGame.SpecialPickup_Rugby_TA
#     │   │   └── Archetypes.SpecialPickups.SpecialPickup_Rugby
#     │   ├── TAGame.SpecialPickup_BallGravity_TA
#     │   │   └── Archetypes.SpecialPickups.SpecialPickup_GravityWell
#     │   ├── TAGame.SpecialPickup_HitForce_TA
#     │   │   └── Archetypes.SpecialPickups.SpecialPickup_StrongHit
#     │   └── TAGame.SpecialPickup_Football_TA
#     │       └── Archetypes.SpecialPickups.SpecialPickup_Football
#     └── TAGame.PickupTimer_TA
#         └── TAGame.Default__PickupTimer_TA
#     TAGame.CrowdManager_TA
#     └── TheWorld:PersistentLevel.CrowdManager_TA
#     TAGame.CrowdActor_TA
#     └── TheWorld:PersistentLevel.CrowdActor_TA
#     TAGame.CameraSettingsActor_TA
#     └── TAGame.Default__CameraSettingsActor_TA
#     TAGame.VehiclePickup_TA
#     ├── TAGame.VehiclePickup_Boost_TA
#     │   └── TheWorld:PersistentLevel.VehiclePickup_Boost_TA
#     └── TAGame.VehiclePickup_Item_TA
#     TAGame.GameEvent_TA
#     └── TAGame.GameEvent_Team_TA
#         └── TAGame.GameEvent_Soccar_TA
#             ├── TAGame.GameEvent_KnockOut_TA
#             │   └── Archetypes.KnockOut.GameEvent_Knockout
#             ├── TAGame.GameEvent_FTE_TA
#             │   └── Archetypes.GameEvent.GameEvent_FTE_Part1_Prime
#             ├── TAGame.GameEvent_Breakout_TA
#             ├── TAGame.GameEvent_Football_TA
#             │   └── GameInfo_FootBall.GameInfo.GameInfo_FootBall:Archetype
#             ├── TAGame.GameEvent_GodBall_TA
#             │   └── GameInfo_GodBall.GameInfo.GameInfo_GodBall:Archetype
#             ├── TAGame.GameEvent_Season_TA
#             │   └── Archetypes.GameEvent.GameEvent_Season
#             ├── TAGame.GameEvent_SoccarPrivate_TA
#             │   ├── TAGame.GameEvent_SoccarSplitscreen_TA
#             │   │   ├── Archetypes.GameEvent.GameEvent_BasketballSplitscreen
#             │   │   ├── Archetypes.GameEvent.GameEvent_HockeySplitscreen
#             │   │   └── Archetypes.GameEvent.GameEvent_SoccarSplitscreen
#             │   ├── Archetypes.GameEvent.GameEvent_BasketballPrivate
#             │   ├── Archetypes.GameEvent.GameEvent_HockeyPrivate
#             │   └── Archetypes.GameEvent.GameEvent_SoccarPrivate
#             ├── TAGame.GameEvent_Tutorial_TA
#             │   ├── TAGame.GameEvent_Tutorial_Goalie_TA
#             │   ├── TAGame.GameEvent_Tutorial_Striker_TA
#             │   └── GameInfo_Tutorial.GameEvent.GameEvent_Tutorial_Aerial
#             ├── TAGame.GameEvent_GameEditor_TA
#             │   └── TAGame.GameEvent_TrainingEditor_TA
#             ├── Archetypes.GameEvent.GameEvent_Basketball
#             ├── Archetypes.GameEvent.GameEvent_Breakout
#             ├── Archetypes.GameEvent.GameEvent_Hockey
#             ├── Archetypes.GameEvent.GameEvent_Items
#             ├── Archetypes.GameEvent.GameEvent_Soccar
#             └── Archetypes.GameEvent.GameEvent_SoccarLan
#     │   ├── Engine.WorldInfo
#     │   └── TAGame.VoteActor_TA
#     │       └── TAGame.Default__VoteActor_TA
#     ├── Engine.Pawn
#     │   └── ProjectX.Pawn_X
#     │       ├── TAGame.RBActor_TA
#     │       │   ├── TAGame.Ball_TA
#     │       │   │   ├── TAGame.Ball_Trajectory_TA
#     │       │   │   ├── TAGame.Ball_Breakout_TA
#     │       │   │   │   └── Archetypes.Ball.Ball_Breakout
#     │       │   │   ├── TAGame.Ball_God_TA
#     │       │   │   │   └── Archetypes.Ball.Ball_God
#     │       │   │   ├── TAGame.Ball_Haunted_TA
#     │       │   │   │   └── Archetypes.Ball.Ball_Haunted
#     │       │   │   ├── Archetypes.Ball.Ball_BasketBall_Mutator
#     │       │   │   ├── Archetypes.Ball.Ball_Basketball
#     │       │   │   ├── Archetypes.Ball.Ball_Beachball
#     │       │   │   ├── Archetypes.Ball.Ball_Default
#     │       │   │   ├── Archetypes.Ball.Ball_Trajectory
#     │       │   │   ├── Archetypes.Ball.Ball_Puck
#     │       │   │   ├── Archetypes.Ball.Ball_Anniversary
#     │       │   │   ├── Archetypes.Ball.CubeBall
#     │       │   │   ├── Archetypes.Ball.Ball_Training
#     │       │   │   └── Archetypes.Ball.Ball_Football
#     │       │   └── TAGame.Vehicle_TA
#     │       │       └── TAGame.Car_TA
#     │       │           ├── Archetypes.GameEvent.GameEvent_Season:CarArchetype
#     │       │           ├── TAGame.Car_Season_TA
#     │       │           ├── TAGame.Car_Freeplay_TA
#     │       │           ├── TAGame.Car_KnockOut_TA
#     │       │           │   └── Archetypes.KnockOut.GameEvent_Knockout:CarArchetype
#     │       │           ├── Archetypes.Car.Car_Default
#     │       │           ├── Archetypes.Car.Car_PostGameLobby
#     │       │           └── TAGame.Default__Car_TA
#     │       └── TAGame.GameEditor_Pawn_TA
#     ├── Engine.DynamicSMActor
#     │   └── Engine.KActor
#     ├── TAGame.BreakOutActor_Platform_TA
#     │   └── TheWorld:PersistentLevel.BreakOutActor_Platform_TA
#     ├── TAGame.InMapScoreboard_TA
#     │   └── TheWorld:PersistentLevel.InMapScoreboard_TA
#     ├── TAGame.HauntedBallTrapTrigger_TA
#     │   └── TheWorld:PersistentLevel.HauntedBallTrapTrigger_TA
#     ├── TAGame.RumblePickups_TA
#     │   └── TAGame.Default__RumblePickups_TA
#     ├── TAGame.Cannon_TA
#     │   └── Archetypes.Tutorial.Cannon
#     ├── TAGame.Stunlock_TA
#     │   └── Archetypes.KnockOut.GameEvent_Knockout:CarArchetype.StunlockArchetype
#     └── TAGame.PlayerStart_Platform_TA
#         └── TheWorld:PersistentLevel.PlayerStart_Platform_TA
# }
