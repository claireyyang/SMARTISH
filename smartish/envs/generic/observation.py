'''
Generic observation holds all of the information that is observable within the simulation. It's created by the state exclusively. The agents use the observations to reason, so only getters are needed.
'''

from . import Board
from typing import List, Tuple


class Observation:
    '''
    A generic observation class to be used by agents to reason about their state based on the observable attributes.
    '''
    def __init__(self, agent_id: int, agent_position: Tuple[int, int], board: Board, signal: List[bool]) -> None:
        '''
        Sets the attributes of the observation, which is from the perspective of the agent specified by the id.
        The agent's position, as well as the signals are observed.
        '''
        self._agent_id: int = agent_id
        self._agent_position: Tuple[int, int] = agent_position
        self._board: Board = board
        self._signal: List[bool] = signal

    def getAgentId(self) -> int:
        return self._agent_id

    def getAgentPosition(self) -> Tuple[int, int]:
        return self._agent_position

    def getBoard(self) -> Board:
        return self._board

    def getSignal(self) -> List[bool]:
        return self._signal
