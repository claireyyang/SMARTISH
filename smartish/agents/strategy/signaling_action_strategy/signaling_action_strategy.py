'''
Module defining agent's social preference signaling action strategy interface and implementing
a few environment independent strategies.
'''
from typing import List, Tuple
from uuid import UUID
from smartish.actions import SignalingActionSpace, SignalingAction
from smartish.agents import AgentMemory
from smartish.envs import State
class SignalingActionStrategy():
    '''
    Interface for defining agent strategies for choosing their social preference
    signaling actions.
    '''
    def act(self, state_beliefs: List[Tuple[State, float]], memory: AgentMemory,
        action_space: SignalingActionSpace) -> SignalingAction:
        '''
        Interface function for choosing a social preference signal action
        given the belief space and the agent's memory
        '''
        raise NotImplementedError()

    def get_id(self) -> UUID:
        '''Returns the unique ID for this action strategy'''
        raise NotImplementedError()


class RandomSignalingActionStrategy(SignalingActionStrategy):
    '''
    A social preference action strategy where the agent chooses their social
    preference signaling action randomly at each time step.
    '''
    def act(self, state_beliefs: List[Tuple[State, float]], memory: AgentMemory,
            action_space: SignalingActionSpace) -> SignalingAction:
        ''' Randomly samples an action from the signaling action space'''
        return SignalingAction(action_space.sample())

    def get_id(self) -> UUID:
        '''Returns the unique ID for this action strategy'''
        raise NotImplementedError()

class TruthfulSignalingActionStrategy(SignalingActionStrategy):
    '''
    A social preference action strategy that where the agent chooses the signaling
    action that matches the social preference action chosen at this time step.
    '''
    def act(self, state_beliefs: List[Tuple[State, float]], memory: AgentMemory,
            action_space: SignalingActionSpace) -> SignalingAction:
        '''
        Returns the signaling action equivalent to the social preference action
        chosen in this time step.
        '''
        # the agent's memory will be updated after they choose their social preference action
        # before they now choose their signaling action.
        return SignalingAction(memory.get_last_social_preference_action())

    def get_id(self) -> UUID:
        '''Returns the unique ID for this action strategy'''
        raise NotImplementedError()


class ProSocialSignalingActionStrategy(SignalingActionStrategy):
    '''
    A social preference signaling action strategy where the agent chooses their signaling
    action to signal a social preference to all other agent's at every time step.
    '''
    def act(self, state_beliefs: List[Tuple[State, float]], memory: AgentMemory,
            action_space: SignalingActionSpace) -> SignalingAction:
        '''
        Returns the signaling action for indicating the agent has a social preference
        to all of the other agents.
        '''
        return SignalingAction(action_space.get_most_prosocial_action())

    def get_id(self) -> UUID:
        '''Returns the unique ID for this action strategy'''
        raise NotImplementedError()


class AntiSocialSignalingActionStrategy(SignalingActionStrategy):
    '''
    A social preference signaling action strategy where the agent chooses their signaling
    action to signal a social preference to no other agent's at every time step.
    '''
    def act(self, state_beliefs: List[Tuple[State, float]], memory: AgentMemory,
            action_space: SignalingActionSpace) -> SignalingAction:
        '''
        Returns the signaling action for indicating the agent has no social preference
        to any of the other agents.
        '''
        return SignalingAction(action_space.get_most_antisocial_action())

    def get_id(self) -> UUID:
        '''Returns the unique ID for this action strategy'''
        raise NotImplementedError()
