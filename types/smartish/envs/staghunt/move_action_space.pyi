from enum import IntEnum
from smartish.actions import DiscreteActionSpace as DiscreteActionSpace
from typing import Tuple

class StaghuntMoveAction(IntEnum):
    STOP: int = ...
    UP: int = ...
    RIGHT: int = ...
    DOWN: int = ...
    LEFT: int = ...

class StaghuntMoveActionSpace(DiscreteActionSpace):
    MOVEMENT_FROM_ACTION: dict[StaghuntMoveAction, Tuple[int, int]] = ...
    ACTION_FROM_MOVEMENT: dict[Tuple[int, int], StaghuntMoveAction] = ...
    def __init__(self) -> None: ...
    @staticmethod
    def get_movement(action: StaghuntMoveAction) -> Tuple[int, int]: ...
    @staticmethod
    def get_action(movement: Tuple[int, int]) -> StaghuntMoveAction: ...
