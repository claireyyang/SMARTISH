'''
Generic state holds all of the information about the current state, regardless of the observability
'''

from . import Observation
from . import Board
from typing import List, Tuple
from smartish.agents import BaseAgent


class State:
    '''
    A generic class for holding attributes about State
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

    def getBoard(self) -> Board:
        return self._board

    def updateBoard(self, new_board: Board) -> None:
        self._board = new_board

    def getStepCount(self) -> int:
        return self._step_count

    def getSignals(self) -> List[List[bool]]:
        return self._signals

    def updateSignals(self, new_signals: List[List[bool]]) -> None:
        self._signals = new_signals

    def getSignalsOfId(self, agent_id: int) -> List[bool]:
        return self._signals[agent_id]

    def updateSignalsOfId(self, agent_id: int, new_signal_of_id: List[bool]) -> None:
        self._signals[agent_id] = new_signal_of_id

    def getHiddenState(self) -> List[List[bool]]:
        return self._hidden_state

    def updateHiddenState(self, new_hidden_state: List[List[bool]]) -> None:
        self._hidden_state = new_hidden_state

    def getHiddenStateOfId(self, agent_id: int) -> List[bool]:
        return self._hidden_state[agent_id]

    def updateHiddenStateOfId(self, agent_id: int, new_hidden_state_of_id: List[bool]) -> None:
        self._hidden_state[agent_id] = new_hidden_state_of_id

    def getObservationFromCurrentState(self, agent: BaseAgent) -> Observation:
        '''
        create the observation from the current state for one particular agent
        '''
        agent_id: int = agent.getAgentId()
        agent_position: Tuple[int, int] = self._board.getPositionOfId(agent_id)
        signal: List[bool] = self.getSignalsOfId(agent_id)
        obs: Observation = Observation(agent_id, agent_position, self._board, signal)
        return obs

    def getObservationsFromCurrentState(self) -> List[Observation]:
        '''
        create the observation from the current state for one particular agent
        '''
        obs_list: List[Observation] = []
        for agent in self._agents:
            agent_id: int = agent.getAgentId()
            agent_position: Tuple[int, int] = self._board.getPositionOfId(agent_id)
            signal: List[bool] = self.getSignalsOfId(agent_id)
            obs: Observation = Observation(agent_id, agent_position, self._board, signal)
            obs_list.append(obs)
        return obs_list
