'''
A module defining an interface for observations to be extended by specific environments.
'''
from typing import List
class Observation():
    '''
    Interface for observations. All observations have the social preference broadcast.
    Additional functionality is provided in subclasses.
    '''
    def __init__(self, social_preference_broadcast:: List[List[bool]]) -> Observation:
        self.social_preference_broadcast = social_preference_broadcast
        

    def get_social_preference_broadcast(self) -> List[List[bool]]:
        '''
        Returns the social preference matrix broadcast by agents at a time step.
        '''
        return self.social_preference_broadcast
