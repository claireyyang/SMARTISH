'''
A module defining specific agent strategies for conveience.

Available agent strategies
    RandomAgentStrategy using
        - NoStateReasoningStrategy
        - NoAgentReasoningStrategy
        - RandomDiscreteActionStrategy
        - RandomSocialPreferenceActionStrategy
        - RandomSignalingActionStrategy
'''
from smartish.agents.strategy import (
    AgentStrategy,
    NoStateReasoningStrategy,
    NoAgentReasoningStrategy,
    RandomDiscreteActionStrategy,
    RandomSocialPreferenceActionStrategy,
    RandomSignalingActionStrategy
)

RandomAgentStrategy = AgentStrategy(
    NoStateReasoningStrategy(), NoAgentReasoningStrategy(), RandomDiscreteActionStrategy(),
    RandomSocialPreferenceActionStrategy(), RandomSignalingActionStrategy()
)
