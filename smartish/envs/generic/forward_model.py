'''
A generic forward model that specifies the general actions/steps of social preferences and signaling
'''
from . import State
from smartish.actions import SocialPreferenceActionSpace
from typing import List
from . import Observation


class ForwardModel:
    '''
    Holds all the functions for a generic forward model that includes social preferences and signaling
    '''
    def __init__(self) -> None:
        '''
        Constructs the Forward Model
        '''
        # self._state = state
        pass

    def socialPreferenceStep(self, state : State, actions: List[SocialPreferenceAction]) -> State:
        '''
        Given social preference actions, returns a new state after taking the social preference step
        '''
        # TODO

    def signalingStep(self, state : State, actions: List[SignalingAction]) -> State:
        '''
        Given signaling actions, returns a new state after taking the signaling step
        '''
        # TODO

    def getObservationFromCurrentState(self, state : State, agent : BaseAgent) -> Observation:
        '''
        Returns the observation from the current state from the point of view of the specified agent
        '''
        return state.getObservationFromCurrentState(agent)

    def getObservationsFromCurrentState(self, state : State, agents : list[BaseAgent]) -> list[Observation]:
        '''
        Returns the observations from the current state for each agent in the list
        '''
        return state.getObservationsFromCurrentState(agent)

    def step(self, state : State, actions: list[IntEnum]) -> State:
        # TODO: put the three different steps in here

    def envSpecificStep(self, state : State, actions: list[StaghuntMoveAction]) -> State:
        raise NotImplementedError
