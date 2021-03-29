'''
A class containing the staghunt board
'''
from ..generic import Board
from typing import Tuple


class StaghuntBoard(Board):
    '''
    A class that holds the basic components for an environment model, viewer, observation_space
    '''
    def __init__(self, board: dict = {}) -> None:
        super().__init__(board)

    def getAgentPosition(self, agent_id: int) -> Tuple[int, int]:
        '''
        Return the tuple that represents the agent's position on the board
        '''
        for key in self._board:
            if self._board[key] == agent_id:
                return key

    def setBoard(self, new_board: dict) -> None:
        '''
        Return the dictionary that represents the board
        '''
        self._board = new_board
