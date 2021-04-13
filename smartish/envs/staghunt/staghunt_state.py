'''
Staghunt state holds all of the information about the current state, regardless of the observability
'''

from ..generic import Board
from typing import List
from smartish.agents import BaseAgent
from typing import Tuple
from ..generic import State
from . import StaghuntObservation


class StaghuntState(State):
    '''
    A staghunt class for holding attributes about State
    '''
    def __init__(self, board: Board, agents: List[BaseAgent],
                 signals: List[List[bool]], hidden_state: List[List[bool]],
                 step_count: int, done: bool) -> None:
        '''
        Sets the attributes of the state, by holding the board info, agents, and current step count
        '''
        self._board: Board = board
        self._agents: List[BaseAgent] = agents
        self._signals: List[List[bool]] = signals
        self._hidden_state: List[List[bool]] = hidden_state
        self._step_count: int = step_count
        self._done: bool = done

        super().__init__(board, agents, signals, hidden_state, step_count, done)

    def getObservationFromCurrentState(self, agent: BaseAgent) -> StaghuntObservation:
        '''
        create the observation from the current state for one particular agent
        '''
        agent_id: int = agent.getAgentId()
        agent_position: Tuple[int, int] = self._board.getPositionOfId(agent_id)
        signal: List[bool] = self.getSignalsOfId(agent_id)
        obs: StaghuntObservation = StaghuntObservation(agent_id, agent_position, self._board, signal)
        return obs

    def getObservationsFromCurrentState(self) -> List[StaghuntObservation]:
        '''
        create the observation from the current state for one particular agent
        '''
        obs_list: List[StaghuntObservation] = []
        for agent in self._agents:
            agent_id: int = agent.getAgentId()
            agent_position: Tuple[int, int] = self._board.getPositionOfId(
                agent_id)
            signal: List[bool] = self.getSignalsOfId(agent_id)
            obs: StaghuntObservation = StaghuntObservation(agent_id, agent_position, self._board, signal)
            obs_list.append(obs)
        return obs_list
