'''
Module containing the move action space in the staghunt environment
and a named constants for the staghunt move actions.
'''
from enum import IntEnum
from typing import Tuple

from smartish.actions import DiscreteActionSpace

class StaghuntMoveAction(IntEnum):
    '''
    Named constants for the Stag Hunt actions
    '''
    STOP = 0
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

class StaghuntMoveActionSpace(DiscreteActionSpace):
    '''
    DOCSTRING
    '''
    # Dictionary that maps a stag hunt action to the movement on the game board
    MOVEMENT_FROM_ACTION : dict[StaghuntMoveAction, Tuple[int,int]] = \
        {StaghuntMoveAction.STOP : (0,0), StaghuntMoveAction.UP : (0,1),
         StaghuntMoveAction.RIGHT : (1,0), StaghuntMoveAction.DOWN : (0,-1),
         StaghuntMoveAction.LEFT : (-1,0)}
    ACTION_FROM_MOVEMENT : dict[Tuple[int,int], StaghuntMoveAction] = \
        {(0,0) : StaghuntMoveAction.STOP, (0,1): StaghuntMoveAction.UP,
         (1,0) : StaghuntMoveAction.RIGHT, (0,-1) : StaghuntMoveAction.DOWN,
         (-1,0) : StaghuntMoveAction.LEFT}

    def __init__(self):
        '''
        Constructs a StaghuntMoveActionSpace which is a discrete action space of
        size 5. There should exist only one of these in your code.
        '''
        super().__init__(5)

    @staticmethod
    def get_movement(action: StaghuntMoveAction) -> Tuple[int,int]:
        '''
        Converts a discrete action to a 2-tuple of movements in the
        x and y direction respectively.
        '''
        return StaghuntMoveActionSpace.MOVEMENT_FROM_ACTION[action]

    @staticmethod
    def get_action(movement: Tuple[int,int]) -> StaghuntMoveAction:
        '''
        Converts a movement in the x and y direction to the corresponding
        move action within the stag hunt move action space.
        '''
        return StaghuntMoveActionSpace.ACTION_FROM_MOVEMENT[movement]
