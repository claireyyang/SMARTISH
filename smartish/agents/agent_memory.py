'''
The interface for agent's memory. It defines thigns that are consistent for agent's
regardless of the environment. It should be extended to add environment specific or
other interesting use cases of memory.
'''
from typing import List, Tuple, Dict, Optional
from smartish.actions import Action, SocialPreferenceAction, SignalingAction
from smartish.agents import AgentId, CognitiveHierarchy
from smartish.agents.strategy import AgentStrategy
from smartish.envs.generic import Observation, State


class AgentMemory():
    ''' The base class for representing an agent's memory. '''
    def __init__(self, memoryLoadFile = None):
        if memoryLoadFile is None:
            self.current_game = GameMemory()
            self.games = [self.current_game]
            self.current_strategy = None

    def set_current_strategy(self, strategy: AgentStrategy) \
        -> None:
        ''' Sets the current strategy profile of the agent. '''
        self.current_strategy = strategy

    def get_current_strategy(self) -> AgentStrategy:
        ''' Gets the current strategy profie of the agent. '''
        return self.current_strategy

    def get_all_observations(self) -> List[List[Observation]]:
        '''
        Gets a matrix of observations from all the games in
        the agent's memory. Each row represents a game where the
        observations are ordered by the time step they occur.
        '''
        return [game.get_observations() for game in self.games]

    def get_game_observations(self) -> List[Observation]:
        ''' Get all the observation for the current game the agent is playing '''
        self.current_game.get_observations()

    def add_observation(self, obs: Observation) -> None:
        '''
        Add an observation to the agent's memory. This observation is assumed to be the most
        recent observation in the current game the agent is playing. '''
        self.current_game.add_observation(obs)

    def get_last_observation(self) -> Observation:
        '''Get the most recent observation from the current game the agent is playing. '''
        return self.current_game.get_last_observation()

    def add_state_beliefs(self, state_beliefs: List[Tuple[State, float]]) -> None:
        '''Add the agent's belief space at the most recent timestep. '''
        self.current_game.add_state_beliefs(state_beliefs)

    def add_env_specific_action(self, action: Action) -> None:
        ''' Add the most recent environment specific action chosen by the agent. '''
        self.current_game.add_env_specific_action(action)

    def add_social_preference_action(self, action: SocialPreferenceAction) -> None:
        ''' Add the most recent social preference action chosen by the agent. '''
        self.current_game.add_social_preference_action(action)

    def add_signaling_action(self, action: SignalingAction) -> None:
        ''' Add the most recent signaling action chosen by the agent. '''
        self.current_game.add_signaling_action(action)

    def add_cognitive_hierarchy_probs(self,
        ch_probs: Optional[Dict[AgentId, Dict[CognitiveHierarchy, float]]]) -> None:
        ''' DOCSTRING '''
        self.current_game.add_cognitive_hierarchy_probs(ch_probs)

    def get_last_cognitive_hierarchy_probs(self, agent_id: AgentId) \
        -> Dict[CognitiveHierarchy, float]:
        ''' DOCSTRING '''
        self.current_game.get_last_cognitive_hierarchy_probs(agent_id)

    def get_last_env_specific_action(self) -> Action:
        ''' DOCSTRING '''
        return self.current_game.get_last_env_specific_action()

    def get_last_signaling_action(self) -> SignalingAction:
        ''' DOCSTRING '''
        return self.current_game.get_last_signaling_action()

    def get_last_social_preference_action(self) -> SocialPreferenceAction:
        ''' DOCSTRING '''
        return self.current_game.get_last_social_preference_action()

class GameMemory():
    ''' CLASS DOCSTRING '''
    def __init__(self):
        self.observations : List[Observation] = []
        self.env_specific_actions : List[Action] = []
        self.social_preference_actions : List[SocialPreferenceAction] = []
        self.signaling_actions : List[SignalingAction] = []
        # A list of dictionaries that map an agent ID to a set of cognitive hierarchies
        # and the probability the agent thinks that agent has that cognitive hierarchies.
        # An entry is added at each time step.
        self.cognitive_hierarchies_probs : \
            List[Optional[Dict[AgentId, Dict[CognitiveHierarchy, float]]]] = []

        self.state_beliefs = List[List[Tuple[State, float]]] = []

    def add_state_beliefs(self, state_beliefs: List[Tuple[State, float]]) -> None:
        ''' DOCSTRING '''
        self.state_beliefs.append(state_beliefs)

    def add_observation(self, obs: Observation) -> None:
        ''' DOCSTRING '''
        self.observations.append(obs)

    def get_observations(self) -> List[Observation]:
        ''' DOCSTRING '''
        return self.observations

    def get_last_observation(self) -> Observation:
        ''' DOCSTRING '''
        return self.observations[-1]

    def add_cognitive_hierarchy_probs(self,
        ch_probs: Optional[Dict[AgentId, Dict[AgentId, Dict[CognitiveHierarchy, float]]]]) -> None:
        ''' DOCSTRING '''
        self.cognitive_hierarchies_probs.append(ch_probs)

    def get_last_cognitive_hierarchy_probs(self, agent_id: AgentId) \
        -> Dict[CognitiveHierarchy, float]:
        ''' DOCSTRING '''
        last_hierarchy_probs = self.cognitive_hierarchies_probs[-1]
        if last_hierarchy_probs is None:
            raise Exception() # TODO: replace with a more specific exception
        try:
            return last_hierarchy_probs[agent_id]
        except KeyError as exc:
            raise Exception() from exc # TODO: replace with a more specific exception

    def add_env_specific_action(self, action: Action) -> None:
        ''' DOCSTRING '''
        self.env_specific_actions.append(action)

    def get_last_env_specific_action(self) -> Action:
        ''' DOCSTRING '''
        return self.env_specific_actions[-1]

    def add_social_preference_action(self, action: SocialPreferenceAction) -> None:
        ''' DOCSTRING '''
        self.social_preference_actions.append(action)

    def get_last_social_preference_action(self) -> SocialPreferenceAction:
        ''' DOCSTRING '''
        return self.social_preference_actions[-1]

    def add_signaling_action(self, action: SignalingAction) -> None:
        ''' DOCSTRING '''
        self.signaling_actions.append(action)

    def get_last_signaling_action(self) -> SignalingAction:
        ''' DOCSTRING '''
        return self.signaling_actions[-1]
