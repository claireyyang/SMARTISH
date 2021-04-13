'''
A module defining an interface for states to be extended by specific environments
'''
from smartish.agents import Agent
class State():

    def get_observation(agent: Agent) -> Observation:
        '''
        Gets an observation for a specific agent at this state
        '''
        raise NotImplementedError()

    def get_observations(agents: List[Agent]) -> List[Observation]:
        '''
        Gets the observations for a set of agents at this state.
        The order the agents are passed in should correspond to the
        order of observations returned.
        '''
        raise NotImplementedError()
