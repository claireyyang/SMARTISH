'''
A class containing the staghunt reward structure.
'''
from .. import Reward
from . import StaghuntState
from smartish.agents import Agent


class StaghuntReward(Reward):
    '''
    A class that holds the reward
    '''
    def __init__(self, state: StaghuntState, agent: Agent) -> None:
        self._reward_amount = 0
        super().__init__()

    def calculateRewardAmount(self, state: StaghuntState, agent: Agent) -> None:
        '''
        Calculate the reward amount based on the state and the agent. Sets the reward_amount in the class.
        '''
        reward = -1


        self._reward_amount = reward
