'''
A module containing the SocialPreferenceActionSpace that should be used to choose social preferences
either as the truth or the broadcast. Also contains a SocialPreferenceConversionError class, that is
raised if there is an error converting social preference actions to the equivalent social preference
list of trues and falses.
'''
from typing import List, Optional
from smartish.actions.discrete_action_space import DiscreteActionSpace
class SocialPreferenceConversionError(RuntimeError):
    '''
    An error that is raised when there is an issue converting to the social preference list
    from the social preference action in the action space. 1 of 3 types of error can occur.
      1. The action provided is not within the expected range.
         The range allowed is 0 to 2^(num_agents-1)-1.
      2. The agent id provided is not within 0 to num_agents-1
         when the action space was initialized.
      3. There was a conversion to a social preference matrix
         and they provided more actions than agents.
    '''
    def __init__(self, num_agents: int, action: Optional[int]=None,
                 actions: Optional[int]=None, agent_id: Optional[int] = None):
        message = "Error converting social preference action to list or matrix\n"
        if action is not None:
            message += (f'Action {action} is not a valid social preference action. '
                       f'The action should range from 0 to {2**num_agents-1}.')
        if actions is not None:
            message += (f'Too many actions provided. {actions} actions were provided, but'
                       f'the action space is only designed for {num_agents} actions.')
        if agent_id is not None:
            message += (f'Agent ID provided is {agent_id}. This action space expects agent'
                       f' ids from 0 to {num_agents-1}.')
        super().__init__(message)

class SocialPreferenceActionSpace(DiscreteActionSpace):
    '''
    A social preference action space. This action space allows agents to specify their
    social preference to all the other agents in the game. The action's binary string
    representation corresponds to the social preference with 1 = True and 0 = False.
    To create a social preference action space, specify how many agents are in the game.
    NOTE: Actions have a different social preference list depending on the agent as the
          agent, by definition, cannot have a social preference to themselves, so their
          index is always False in the social preference list.
    '''
    def __init__(self, num_agents: int) -> None:
        # It's minus one since agents can't have a
        # "social preference" for themselves.
        # This means the action is different depending on
        # the agent id
        super().__init__(2**(num_agents-1))
        self.num_agents = num_agents

    def convert_to_social_preference_list(self, agent_id: int, action: int) -> List[bool]:
        '''
        Convert an action in this discrete action space to a list of social preferences from
        a given agent's perspective.
        If performance issues are a concern, this could turn into a dictionary lookup instead
        if the number of agents is small
        '''
        # Get the binary representation of an int.
        # Uses zfill to pad with zeros where appropriate
        if agent_id >= self.num_agents or agent_id < 0:
            raise SocialPreferenceConversionError(self.num_agents, agent_id=agent_id)
        if action >= self.action_space_size or action < 0:
            raise SocialPreferenceConversionError(self.num_agents, action=action)
        binary_rep: str = format(action, 'b').zfill(self.num_agents-1)
        print(binary_rep)
        social_preference_list: List[bool] = [False]*self.num_agents
        # This is used to shift the values of the binary number/social preference list
        # so that we insert a 0 at the agent's position within the binary string of the action.
        # It is initially 0 and changed to 1 after we traverse pass the agent_id
        idx_adjuster : int = 0
        for idx, bit in enumerate(binary_rep):
            # Start adjusting the indices since we've passed the agent's id
            if idx == agent_id:
                idx_adjuster = 1
            if bit == '1':
                social_preference_list[idx+idx_adjuster] = True
        return social_preference_list

    def convert_to_social_preference_matrix(self, actions: List[int]) -> List[List[bool]]:
        '''
        Converts a list of actions to a matrix of boolean social preferences where each row
        is an agent's specified social preference list with all the diagonals set to false
        as an agent, by definition, cannot have "social preference" to itself. Actions are
        expected to be given in order of agent ID.
        '''
        if len(actions) > self.num_agents:
            raise SocialPreferenceConversionError(self.num_agents, actions = len(actions))
        social_preference_matrix = []
        for agent_id, action in enumerate(actions):
            social_preference_matrix.append(
                self.convert_to_social_preference_list(agent_id, action))
        return social_preference_matrix
