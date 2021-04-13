'''
This module defines a wrapper for the 5 strategies that define an agent
'''
from typing import List, Tuple, Dict, Optional
from smartish.actions import (
    Action, SocialPreferenceAction, SignalingAction,
    DiscreteActionSpace, SocialPreferenceActionSpace, SignalingActionSpace)
#from smartish.agents.agent_memory import AgentMemory
from smartish.agents import AgentId, CognitiveHierarchy, AgentMemory
from smartish.agents.strategy.agent_reasoning_strategy import AgentReasoningStrategy
from smartish.agents.strategy.env_specific_action_strategy import EnvSpecificActionStrategy
from smartish.agents.strategy.social_preference_action_strategy import (
    SocialPreferenceActionStrategy
)
from smartish.agents.strategy.signaling_action_strategy import SignalingActionStrategy
from smartish.agents.strategy.state_reasoning_strategy import StateReasoningStrategy
from smartish.envs import State, Observation

class AgentStrategy():
    '''
    CLASS DOCSTRING
    '''
    #pylint: disable=too-many-arguments
    def __init__(self,
        state_reasoning_strategy : StateReasoningStrategy,
        agent_reasoning_strategy : AgentReasoningStrategy,
        env_specific_action_strategy : EnvSpecificActionStrategy,
        social_preference_action_strategy : SocialPreferenceActionStrategy,
        signaling_action_strategy : SignalingActionStrategy
    ):
        self.state_reasoning_strategy = state_reasoning_strategy
        self.agent_reasoning_strategy = agent_reasoning_strategy
        self.env_specific_action_strategy = env_specific_action_strategy
        self.social_preference_action_strategy = social_preference_action_strategy
        self.signaling_action_strategy = signaling_action_strategy

    def reason_about_state(self, obs: Observation, memory: AgentMemory) \
        -> List[Tuple[State, float]]:
        ''' Uses the state reasoning strategy to reason about the state '''
        return self.state_reasoning_strategy.reason(obs, memory)

    def reason_about_agents(self, state_beliefs : List[Tuple[State, float]], memory: AgentMemory) \
        -> Optional[Dict[AgentId, Dict[CognitiveHierarchy, float]]]:
        ''' Uses the agent reasoning strategy to reason about other agents '''
        return self.agent_reasoning_strategy.reason(state_beliefs, memory)

    def env_act(self, state_beliefs : List[Tuple[State, float]], memory: AgentMemory,
        action_space: DiscreteActionSpace) -> Action:
        ''' Uses the environment specific action strategy to choose an action '''
        return self.env_specific_action_strategy.act(state_beliefs, memory, action_space)

    def social_preference_act(self, state_beliefs : List[Tuple[State, float]], memory: AgentMemory,
        action_space: SocialPreferenceActionSpace) -> SocialPreferenceAction:
        ''' Uses the social preference action strategy to choose an action '''
        return self.social_preference_action_strategy.act(state_beliefs, memory, action_space)

    def signal_act(self, state_beliefs : List[Tuple[State, float]], memory: AgentMemory,
        action_space: SignalingActionSpace) -> SignalingAction:
        ''' Uses the signaling action strategy to choose an action '''
        return self.signaling_action_strategy.act(state_beliefs, memory, action_space)
