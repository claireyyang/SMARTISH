'''
A module defining the environment specific action strategy interface.
'''
from typing import List, Tuple
from uuid import UUID
from smartish.actions import DiscreteActionSpace, Action
from smartish.agents import AgentMemory
from smartish.envs import State

class EnvSpecificActionStrategy():
    '''
    The interface for an action strategy for a specific environment.
    '''
    def act(self, state_beliefs: List[Tuple[State, float]], memory: AgentMemory,
        action_space: DiscreteActionSpace) -> Action:
        '''
        The act function which takes the belief space and memory of an agent
        and returns an action within the given action space.
        '''
        raise NotImplementedError()

    def get_id(self) -> UUID:
        '''Returns the unique ID for this action strategy'''
        raise NotImplementedError()

class RandomDiscreteActionStrategy(EnvSpecificActionStrategy):
    '''
    An action strategy that chooses a random action from the action space.
    '''
    def act(self, state_beliefs: List[Tuple[State, float]], memory: AgentMemory,
            action_space: DiscreteActionSpace) -> Action:
        '''Samples an action from the action space'''
        return action_space.sample()

    def get_id(self) -> UUID:
        '''Returns the unique ID for this action strategy'''
        raise NotImplementedError()
