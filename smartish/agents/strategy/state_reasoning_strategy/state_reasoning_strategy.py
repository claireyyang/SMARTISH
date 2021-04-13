'''
A module defining the strategy based on how the agent reasons
about what state they are in.
'''
from typing import List, Tuple
from uuid import UUID
from smartish.agents import AgentMemory
from smartish.envs import Observation, State
class StateReasoningStrategy():
    '''
    The interface class that defines the method that should be implemented by state
    reasoning strategies.
    '''
    def reason(self, obs: Observation, memory: AgentMemory) -> List[Tuple[State, float]]:
        '''
        Interface function that state reasoning strategies need to follow.
        This interface takes in a new observation and the agent's memory and returns
        a list of state, probability pairs
        '''
        raise NotImplementedError()

    def get_id(self) -> UUID:
        '''Returns the unique ID for this action strategy'''
        raise NotImplementedError()

class NoStateReasoningStrategy(StateReasoningStrategy):
    '''
    A class defining a strategy where the agent does not reason at all about
    what state they are in. Thus, when reason is called they return an empty list
    of state, probability pairs.
    '''
    def reason(self, obs: Observation, memory: AgentMemory) -> List[Tuple[State, float]]:
        '''
        As this strategy does no reasoning it just immediately returns an empty list
        '''
        return []

    def get_id(self) -> UUID:
        '''Returns the unique ID for this action strategy'''
