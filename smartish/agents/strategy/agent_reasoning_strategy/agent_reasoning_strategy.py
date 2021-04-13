'''
A module defining the strategy based on how an agent reasons about other agents.
'''
from typing import Optional, Dict, List, Tuple
from uuid import UUID
from smartish.agents import AgentId, AgentMemory, CognitiveHierarchy
from smartish.envs import State

class AgentReasoningStrategy():
    '''
    The interface for agent reasoning strategies. Agent reasoning takes place by
    using the agent's memory and their current state beliefs and returns a
    mapping from AgentID to a set of cognitive hierarchies and the associated
    probability the agent has that hierarchy (also stored as a dictionary).
    '''
    def reason(self, state_beliefs: List[Tuple[State, float]], memory: AgentMemory) \
        -> Optional[Dict[AgentId, Dict[CognitiveHierarchy, float]]]:
        '''
        Interface function that agent reasoning strategies need to follow.
        This interface takes in the current belief space of the agent along with their
        memory and returns an optional mapping of agent IDs to their possible cognitive
        hierarchies and the probabilities the agent belief's they have that hierarchy.
        '''
        raise NotImplementedError()

    def get_id(self) -> UUID:
        ''' Returns the unique ID associating with this agent reasoning strategy'''
        raise NotImplementedError()

class NoAgentReasoningStrategy(AgentReasoningStrategy):
    '''
    A class representing a generic agent reasoning strategy where the
    agent does not reason about the other agents at all. This would be the strategy
    of a base or level 0 agent. It returns None from reasoning.
    '''
    def reason(self, state_beliefs: List[Tuple[State, float]], memory: AgentMemory) \
        -> Optional[Dict[AgentId, Dict[CognitiveHierarchy, float]]]:
        '''
        As this is the no agent reasoning strategy, it does nothing and returns None
        '''
        return None

    def get_id(self) -> UUID:
        ''' Returns the unique ID associating with this agent reasoning strategy'''
        raise NotImplementedError()

class SetAgentReasoningStrategy(AgentReasoningStrategy):
    '''
    A class representing a generic agent reasoning strategy where the agent has
    set thoughts about the cognitive hierarchy of other agents. These thoughts are set
    when the strategy is constructed by passing in a map that maps an agent ID to a cognitive
    hierarchy. The hierarchies are absolute meaning the agent with this strategy thinks the
    other agent's have these hierarchies with probability 1.
    '''
    def __init__(self, set_cognitive_hierarchies: Dict[AgentId, CognitiveHierarchy]):
        self.cognitive_hierarchy_probs : Dict[AgentId, Dict[CognitiveHierarchy, float]] = dict()
        for agent_id, hierarchy in set_cognitive_hierarchies:
            self.cognitive_hierarchy_probs[agent_id] = {hierarchy: 1.0}

    def reason(self, state_beliefs: List[Tuple[State, float]], memory: AgentMemory) \
        -> Optional[Dict[AgentId, Dict[CognitiveHierarchy, float]]]:
        '''
        Returns the cognitive hierarchies set when the strategy was initialized.
        '''
        return self.cognitive_hierarchy_probs

    def get_id(self) -> UUID:
        ''' Returns the unique ID associating with this agent reasoning strategy'''
        raise NotImplementedError()
