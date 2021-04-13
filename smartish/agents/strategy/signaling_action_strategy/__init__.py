'''
High-level module defining the interface for agent's social preference signaling action strategy
along with some environment independent strategies
'''
from smartish.agents.strategy.signaling_action_strategy import (
    SignalingActionStrategy,
    RandomSignalingActionStrategy,
    TruthfulSignalingActionStrategy,
    ProSocialSignalingActionStrategy,
    AntiSocialSignalingActionStrategy
)

_all_ = [ "SignalingActionStrategy", "RandomSignalingActionStrategy",
    "TruthfulSignalingActionStrategy", "ProSocialSignalingActionStrategy",
    "AntiSocialSignalingActionStrategy" ]
