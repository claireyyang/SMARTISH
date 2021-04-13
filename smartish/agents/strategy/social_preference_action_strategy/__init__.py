'''
High-level module defining the interface for agent's social preference action strategy
along with some environment independent strategies
'''
from smartish.agents.strategy.social_preference_action_strategy import (
    SocialPreferenceActionStrategy,
    RandomSocialPreferenceActionStrategy,
    AntiSocialPreferenceActionStrategy,
    ProSocialPreferenceActionStrategy,
)

__all__ = ["SocialPreferenceActionStrategy", "RandomSocialPreferenceActionStrategy",
    "AntiSocialPreferenceActionStrategy", "ProSocialPreferenceActionStrategy"
]
