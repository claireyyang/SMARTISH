'''
A class containing the staghunt pseudo-reward structure.
'''
from .. import PseudoReward
from . import StaghuntState
from smartish.agents import Agent


class StaghuntPseudoReward(PseudoReward):
    '''
    A class that holds the reward
    '''
    def __init__(self, state: StaghuntState, agent: Agent) -> None:
        self._pseudo_reward_amount = 0
        super().__init__()

    def calculatePseudoRewardAmount(self, state: StaghuntState,
                              agent: Agent) -> None:
        '''
        Calculate the reward amount based on the state and the agent. Sets the pseudo reward_amount in the class.
        '''
        reward = -1
        self._pseudo_reward_amount = reward
