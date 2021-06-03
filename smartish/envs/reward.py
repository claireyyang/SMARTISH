'''
A class containing the reward structure.
'''


class Reward:
    '''
    A class that holds the reward
    '''
    def __init__(self) -> None:
        self._cumulative_reward_amount = 0
        self._reward_amount = 0

    def updateCumulativeRewardAmount(self, new_reward: float) -> None:
        self._cumulative_reward_amount += new_reward

    def getCumulativeRewardAmount(self) -> float:
        return self._cumulative_reward_amount

    def updateRewardAmount(self, new_reward: float) -> None:
        self._reward_amount += new_reward

    def getRewardAmount(self) -> float:
        return self._reward_amount
