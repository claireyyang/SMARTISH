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

    def get_board(self) -> dict:
        '''
        Return the dictionary that represents the board
        '''
        return self._board

    def set_board(self, new_board: dict) -> None:
        '''
        Return the dictionary that represents the board
        '''
        self._board = new_board

    def get_position_of_id(self, id: int) -> Tuple[int, int]:
        '''
        Return the position in the board of the character specified in the id
        '''
        for pos in self._board:
            if self._board[pos] == id:
                return pos
