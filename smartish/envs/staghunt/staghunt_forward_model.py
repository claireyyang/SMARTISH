'''
A staghunt-specific forward model that specifies how the agents move on the board
'''
from ..generic import State
from ..generic import ForwardModel
from ..actions import DiscreteActionSpace
from . import StaghuntMoveActionSpace
from . import StaghuntMoveAction
from enum import IntEnum
from typing import List, Tuple
import typing


class StaghuntForwardModel(ForwardModel):
    '''
    Holds all the functions for a staghunt-specific forward model that includes how the agents move on the board and their reward
    '''
    def __init__(self) -> None:
        super.__init__()

    def act(self, listStates: List[Tuple[State, float]], socialPreferenceActionSpace: SocialPreferenceActionSpace, signalingActionSpace: SignalingActionSpace, moveActionSpace: MoveActionSpace) -> List[Tuple[SignalingAction, SocialPreferenceAction, StaghuntMoveAction]]:
        '''
        call signalingAct, socialPreferenceAct, and staghuntMoveAct for an agent
        '''
        # if state.getStepCount % 3 == 0:
        #     return socialPreferenceAct(discreteActionSpace)
        # elif state.getStepCount % 3 == 1:
        #     return signalingAct(discreteActionSpace)
        # elif state.getStepCount % 3 == 2:
        #     return staghuntMoveAct(discreteActionSpace)

        listActions = []
        # TODO: use the different spaces to figure out the actions we want

        return listActions

    def step(self, state : State, actions: List[IntEnum]) -> State:
        '''
        Determines whether to call signalingStep, socialPreferenceStep, staghuntMoveStep
        '''
        action_example = actions[0]
        if isinstance(action_example, SocialPreferenceAction):
            return socialPreferenceStep(state, actions)
        elif isinstance(action_example, SignalingAction):
            return signalingStep(state, actions)
        elif isinstance(action_example, StaghuntMoveAction):
            return staghuntMoveStep(state, actions)

    def envSpecificStep(self, state : State, actions: list[StaghuntMoveAction]) -> State:
        '''
        Given staghunt move actions, returns a new state after taking the staghunt move step
        '''
        # TODO

    def getDone(self, state : State) -> bool:
        '''
        Returns whether the state passed in means that the game is done
        '''
        # TODO: put in the logic for whether the game is done here, based on the state of the board
