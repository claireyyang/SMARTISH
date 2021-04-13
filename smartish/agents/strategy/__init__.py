'''
A module that combines the 5 different strategies required to define an agent into one
module for ease of imports for other programs.
'''
from smartish.agents.strategy import AgentStrategy
from smartish.agents.strategy.strategies import RandomAgentStrategy
from smartish.agents.strategy.agent_reasoning_strategy import *
from smartish.agents.strategy.env_specific_action_strategy import *
from smartish.agents.strategy.signaling_action_strategy import *
from smartish.agents.strategy.social_preference_action_strategy import *
from smartish.agents.strategy.state_reasoning_strategy import *

_all__ = [
    "AgentReasoningStrategy", "NoAgentReasoningStrategy", "SetAgentReasonigStrategy",

    "EnvSpecificActionStrategy", "RandomDiscreteActionStrategy"

    "SignalingActionStrategy", "RandomSignalingActionStrategy",
    "TruthfulSignalingActionStrategy", "ProSocialSignalingActionStrategy",
    "AntiSocialSignalingActionStrategy",

    "SocialPreferenceActionStrategy", "RandomSocialPreferenceActionStrategy",
    "AntiSocialPreferenceActionStrategy", "ProSocialPreferenceActionStrategy"

    "StateReasoningStrategy", "NoStateReasoningStrategy",

    "RandomAgentStrategy"
]
