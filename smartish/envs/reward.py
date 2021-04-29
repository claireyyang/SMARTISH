'''
A class containing the reward structure.
'''


class Reward:
    '''
    A class that holds the reward
    '''
    def __init__(self) -> None:
        self._reward_amount = 0

    def getRewardAmount(self) -> int:
        return self._reward_amount
