from abc import ABC, abstractmethod
from ex1.capabilities import HealCapability, TransformCapability
from .exceptions import InvalidStrategyError


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature):
        pass

    @abstractmethod
    def is_valid(self, creature):
        pass

    def perform(self, creature):
        if not self.is_valid(creature):
            strategy_name = type(self).__name__.replace("Strategy", "").lower()
            raise InvalidStrategyError(
                f"Invalid Creature '{creature._name}' for this {strategy_name} strategy"
            )
        return self.act(creature)


class NormalStrategy(BattleStrategy):
    def act(self, creature):
        return creature.attack()

    def is_valid(self, creature):
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self, creature):
        return f"{creature.transform()}\n{creature.attack()}\n{creature.revert()}"

    def is_valid(self, creature):
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def act(self, creature):
        return f"{creature.attack()}\n{creature.heal()}"

    def is_valid(self, creature):
        return isinstance(creature, HealCapability)
