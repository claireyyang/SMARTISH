'''
Module defining agent's social preference action strategy interface and implementing
a few environment independent strategies.
'''
from typing import List, Tuple
from uuid import UUID
from smartish.actions import SocialPreferenceActionSpace, SocialPreferenceAction
from smartish.agents import AgentMemory
from smartish.envs import State

class SocialPreferenceActionStrategy():
    '''
    Interface for defining agent strategies for choosing their social preference
    actions.
    '''
    def act(self, state_beliefs: List[Tuple[State, float]], memory: AgentMemory,
            action_space: SocialPreferenceActionSpace) -> SocialPreferenceAction:
        '''
        Interface function for choosing a social preference action given the belief
        space and the agent's memory.
        '''
        raise NotImplementedError()

    def get_id(self) -> UUID:
        '''Returns the unique ID for this action strategy'''
        raise NotImplementedError()

class RandomSocialPreferenceActionStrategy(SocialPreferenceActionStrategy):
    '''
    A social preference action strategy where the agent chooses their social
    preference action randomly at each time step.
    '''
    def act(self, state_beliefs: List[Tuple[State, float]], memory: AgentMemory,
            action_space: SocialPreferenceActionSpace) -> SocialPreferenceAction:
        ''' Randomly samples an action from the social preference action space'''
        return SocialPreferenceAction(action_space.sample())

    def get_id(self) -> UUID:
        '''Returns the unique ID for this action strategy'''
        raise NotImplementedError()

class AntiSocialPreferenceActionStrategy(SocialPreferenceActionStrategy):
    '''
    A social preference action strategy where the agent chooses their social
    preference action to have a social preference for no other agent's at
    every time step.
    '''
    def act(self, state_beliefs: List[Tuple[State, float]], memory: AgentMemory,
            action_space: SocialPreferenceActionSpace) -> SocialPreferenceAction:
        '''
        Returns the social preference action indicating they have social preference
        for none of the other agents.
        '''
        return action_space.get_most_antisocial_action()

    def get_id(self) -> UUID:
        '''Returns the unique ID for this action strategy'''
        raise NotImplementedError()


class ProSocialPreferenceActionStrategy(SocialPreferenceActionStrategy):
    '''
    A social preference action strategy where the agent chooses their social
    preference action to have a social preference for all other agent's at
    every time step.
    '''
    def act(self, state_beliefs: List[Tuple[State, float]], memory: AgentMemory,
            action_space: SocialPreferenceActionSpace) -> SocialPreferenceAction:
        '''
        Returns the social preference action indicating they have social preference
        for every other agent.
        '''
        return action_space.get_most_prosocial_action()

    def get_id(self) -> UUID:
        '''Returns the unique ID for this action strategy'''
        raise NotImplementedError()
