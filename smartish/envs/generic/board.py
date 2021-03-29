'''
A class containing the generic board that the stag hunt board will inherit from
'''


class Board:
    '''
    A class that holds the basic components for an environment model, viewer, observation_space
    '''
    def __init__(self, board: dict = {}) -> None:
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
