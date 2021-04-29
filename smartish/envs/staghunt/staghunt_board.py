'''
A class containing the staghunt board that is set by and updated by the state exclusively.
'''

from typing import Tuple, List
from .. import Board


class StaghuntBoard(Board):
    '''
    A class that holds the physical information about the physical board, as well as the agent positions, stag position, and hare position.
    '''
    def __init__(self, board: dict = dict(), agent_positions: List[Tuple[int, int]], stag_position: Tuple[int, int], hare_position: Tuple[int, int]) -> None:
        self._board: dict = board
        self._agent_positions = agent_positions
        self._stag_position = stag_position
        self._hare_position = hare_position

        super().__init__(board)

    def getAgentPositionOfId(self, agent_id: int) -> Tuple[int, int]:
        return self._agent_positions[agent_id]

    def getAgentPositions(self) -> List[Tuple[int, int]]:
        return self._agent_positions

    def getStagPosition(self) -> Tuple[int, int]:
        return self._stag_position

    def getHarePosition(self) -> Tuple[int, int]:
        return self._hare_position
