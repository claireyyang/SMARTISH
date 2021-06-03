'''
A class containing the pseudo-reward structure.
'''


class PseudoReward:
    '''
    A class that holds the pseudo-reward
    '''
    def __init__(self) -> None:
        self._cumulative_pseudo_reward_amount = 0
        self._pseudo_reward_amount = 0

    def updateCumulativePseudoRewardAmount(self, new_reward: float) -> None:
        self._cumulative_pseudo_reward_amount += new_reward

    def getCumulativePseudoRewardAmount(self) -> float:
        return self._cumulative_pseudo_reward_amount

    def updatePseudoRewardAmount(self, new_reward: float) -> None:
        self._pseudo_reward_amount += new_reward

    def getPseudoRewardAmount(self) -> float:
        return self._pseudo_reward_amount
