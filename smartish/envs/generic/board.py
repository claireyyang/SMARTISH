'''
A class containing the board that is set by and updated by the state exclusively.
'''

from typing import Tuple, List


class Board:
    '''
    A class that holds the physical information about the agents' positions and physical board state.
    '''
    def __init__(self, board: dict = dict()) -> None:
        self._board: dict = board

    def getBoard(self) -> dict:
        '''
        Return the dictionary that represents the board
        '''
        return self._board

    def setBoard(self, new_board: dict) -> None:
        '''
        Return the dictionary that represents the board
        '''
        self._board = new_board

    def getPositionOfId(self, id: int) -> Tuple[int, int]:
        '''
        Return the position in the board of the character specified in the id
        '''
        for pos in self._board:
            if self._board[pos] == id:
                return pos
