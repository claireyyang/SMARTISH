'''
High-Level module for the environment specific action strategy interface and standard
implementations
'''
from smartish.agents.strategy.env_specific_action_strategy import (
    EnvSpecificActionStrategy,
    RandomDiscreteActionStrategy
)

__all__ = [ "EnvSpecificActionStrategy", "RandomDiscreteActionStrategy" ]
