#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   strategies.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/21 10:12:30 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/21 10:47:18 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod
from typing import cast
from ex0.creatures import Creature
from ex1.capabilities import HealCapability, TransformCapability
from .exceptions import InvalidStrategyError


class BattleStrategy(ABC):
    @abstractmethod
    def act(self, creature: Creature) -> str:
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass

    def perform(self, creature: Creature) -> str:
        if not self.is_valid(creature):
            strategy_name = type(self).__name__.replace("Strategy", "").lower()
            raise InvalidStrategyError(
                f"Invalid Creature '{creature._name}'"
                f"for this {strategy_name} strategy"
            )
        return self.act(creature)


class NormalStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        return creature.attack()

    def is_valid(self, creature: Creature) -> bool:
        return True


class AggressiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        c = cast(TransformCapability, creature)
        return f"{c.transform()}\n{creature.attack()}\n{c.revert()}"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)


class DefensiveStrategy(BattleStrategy):
    def act(self, creature: Creature) -> str:
        c = cast(HealCapability, creature)
        return f"{creature.attack()}\n{c.heal()}"

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)
