'''
A module containing discrete action spaces
'''
from __future__ import annotations
from gym import spaces
class DiscreteActionSpace:
    '''
    A class representing an iterable discrete action space. An action space
    initalized with action space size of n is represented using (0,1,...,n-1)
    '''
    def __init__(self, action_space_size: int) -> None:
        self.open_ai_gym_space = spaces.Discrete(action_space_size)
        self.action_space_size : int = action_space_size
        # Variable that keeps track of the "current" action when looping
        # through the action sapce
        self._cur_action : int = 0

    def __iter__(self) -> DiscreteActionSpace:
        self._cur_action = 0
        return self

    def __next__(self) -> int:
        if self._cur_action < self.action_space_size:
            result = self._cur_action
            self._cur_action += 1
            return result
        raise StopIteration

    def __eq__(self, other: object) -> bool:
        return (isinstance(other, DiscreteActionSpace) and
               self.action_space_size == other.action_space_size)

    def sample(self) -> int:
        '''
        Sample an action from the action space
        '''
        return self.open_ai_gym_space.sample()

    def getOpenAIGymActionSpace(self):
        '''
        Get the underlying Open AI gym action space
        '''
        return self.open_ai_gym_space
