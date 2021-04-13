'''
MODULE DOCSTRING
'''
from typing import NewType, Dict, List, Tuple, Optional
from smartish.actions import (
    Action, SocialPreferenceAction, SignalingAction,
    DiscreteActionSpace)
from smartish.agents.agent_memory import AgentMemory
from smartish.agents.strategy import AgentStrategy
from smartish.envs.generic import State, Observation

AgentId = NewType('AgentId', int)
class Agent():
    '''
    CLASS DOCSTRING
    '''
    # ALSO HAVE AGENT TYPE
    # ALSO NEED TO LOAD AGENT'S MEMORY
    def __init__(self,
        agent_game_id: AgentId,
        memory: AgentMemory,
        strategy: AgentStrategy,
    ):
        self.agent_game_id : AgentId = agent_game_id
        self.memory : AgentMemory = memory
        self.strategy : AgentStrategy = strategy
        self.memory.set_current_strategy(strategy)

    def act(self, obs: Observation, action_spaces: DiscreteActionSpace) \
            -> Tuple[Action, SocialPreferenceAction, SignalingAction]:
        '''
        DOCSTRING
        '''
        self.memory.add_observation(obs)
        state_beliefs : List[Tuple[State, float]] = self.strategy.reason_about_state(
            obs, self.memory
        )
        self.memory.add_state_beliefs(state_beliefs)
        ch_probs : Optional[Dict[AgentId, Dict[CognitiveHierarchy, float]]] = \
            self.strategy.reason_about_agents(state_beliefs, self.memory)
        self.memory.add_cognitive_hierarchy_probs(ch_probs)
        # Do the action strategy
        env_specific_action : Action = self.strategy.act(
            state_beliefs, self.memory, self.env_specific_action_space
        )
        self.memory.add_env_specific_action(action)
        social_preference_action : SocialPreferenceAction = self.social_preference_strategy(
            state_beliefs, self.memory, self.env_specific_action, self.signal_strategy)

    def get_agent_id(self) -> AgentId:
        ''' DOCSTRING'''
        return self.agent_game_id
