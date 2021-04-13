'''
Staghunt observation holds all of the information that is observable within the simulation. It's created by the state exclusively. The agents use the observations to reason, so only getters are needed.
'''

from ..generic import Observation
from . import Board
from typing import List, Tuple


class StaghuntObservation(Observation):
    '''
    A staghunt observation class to be used by agents to reason about their state based on the observable attributes.
    The only addition to the StaghuntObservation from the generic Observation is the hare and stag positions
    '''
    def __init__(self, agent_id: int, agent_position: Tuple[int, int],
                 board: Board, signal: List[bool]) -> None:
        '''
        Sets the attributes of the observation, which is from the perspective of the agent specified by the id.
        The agent's position, as well as the signals are observed.
        '''
        self._agent_id: int = agent_id
        self._agent_position: Tuple[int, int] = agent_position
        self._board: Board = board
        self._signal: List[bool] = signal

        super().__init__(agent_id, agent_position, board, signal)

    def getStagPosition(self, stag_id: int) -> Tuple[int, int]:
        # TODO: get the stag int from the constants
        return self._board.getPositionOfId(stag_id)

    def getHarePosition(self, hare_id: int) -> Tuple[int, int]:
        # TODO: get the stag int from the constants
        return self._board.getPositionOfId(hare_id)
