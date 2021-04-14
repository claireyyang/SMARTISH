'''
Staghunt state holds all of the information about the current state, regardless of the observability
'''

from . import StaghuntBoard
from typing import List
from smartish.agents import Agent
from typing import Tuple
from ..generic import State
from . import StaghuntObservation


class StaghuntState(State):
    '''
    A staghunt class for holding attributes about State
    '''
    def __init__(self, board: StaghuntBoard, agents: List[Agent],
                 signals: List[List[bool]], hidden_state: List[List[bool]],
                 step_count: int, done: bool) -> None:
        '''
        Sets the attributes of the state, by holding the board info, agents, and current step count
        '''
        self._board: StaghuntBoard = board
        self._agents: List[Agent] = agents
        self._signals: List[List[bool]] = signals
        self._hidden_state: List[List[bool]] = hidden_state
        self._step_count: int = step_count
        self._done: bool = done

        super().__init__(board, agents, signals, hidden_state, step_count, done)


    def getAgentPosition(self, agent_id: int) -> Tuple[int, int]:
        return self._agent_positions[agent_id]

    def getObservationFromCurrentState(self, agent: Agent) -> StaghuntObservation:
        '''
        create the observation from the current state for one particular agent
        '''
        agent_id: int = agent.getAgentId()
        signal: List[bool] = self.getSignalsOfId(agent_id)
        obs: StaghuntObservation = StaghuntObservation(agent_id, self._board, signal)
        return obs

    def getObservationsFromCurrentState(self) -> List[StaghuntObservation]:
        '''
        create the observation from the current state for one particular agent
        '''
        obs_list: List[StaghuntObservation] = []
        for agent in self._agents:
            agent_id: int = agent.getAgentId()
            signal: List[bool] = self.getSignalsOfId(agent_id)
            obs: StaghuntObservation = StaghuntObservation(agent_id, self._board, signal)
            obs_list.append(obs)
        return obs_list
