'''
A class containing the base environment that all of the environments in each simulation will inherit from
'''
from . import ForwardModel
from . import Viewer
from . import State
from ..agents import BaseAgent

import gym
from gym import spaces

import numpy as np

class BaseEnv(gym.Env):
    '''
    Base Environment
    '''
    def __init__(self, model: ForwardModel,
                 viewer: Viewer,
                 state: State = None,
                 agents: list[BaseAgent] = None) -> None:
        '''
        Constructs the Base Environment
        '''
        self._model: ForwardModel = model
        self._viewer: Viewer = viewer

        self._state = state
        self._agents = agents

        self._step_count = 0
        self.setObservationSpace()

    def setObservationSpace(self) -> None:
        '''
        Set an observation space for the environment
        '''
        bss = self._board_size**2

        # min_obs = all board positions + my position + teammates positions
        min_obs = [0] * bss + [0]*12
        max_obs = [0] * bss + [0]*12
        self._observation_space = spaces.Box(np.array(min_obs), np.array(max_obs))

    def setAgents(self, new_agents: list[BaseAgent]) -> None:
        self._agents = new_agents

    # def reset(self) -> None:
    #     assert (self._agents is not None)

    #     if self._init_game_state is not None:
    #         self.set_json_info()
    #     else:
    #         self._step_count = 0
    #         self.make_board()
    #         for agent_id, agent in enumerate(self._agents):
    #             agent.agent_id = agent_id
    #             agent.reset(self._board)

    #     return self.get_observations()
