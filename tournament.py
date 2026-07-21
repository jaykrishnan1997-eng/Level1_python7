#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   tournament.py                                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/21 10:08:23 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/21 11:26:27 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from typing import List, Tuple
from ex0 import FlameFactory, AquaFactory
from ex0.factories import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    NormalStrategy, AggressiveStrategy,
    DefensiveStrategy, InvalidStrategyError
)
from ex2.strategies import BattleStrategy


def battle(opponents: List[Tuple[CreatureFactory, BattleStrategy]]) -> None:
    summary = ", ".join(
        f"({f.label}+{type(s).__name__.replace('Strategy', '')})"
        for f, s in opponents
    )
    print(f"[ {summary} ]")
    print(f"*** Tournament ***\n{len(opponents)} opponents involved")
    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            creature1 = factory1.create_base()
            creature2 = factory2.create_base()

            print("\n* Battle *")
            print(f"{creature1.describe()}\n vs.\n{creature2.describe()}")
            print(" now fight!")

            try:
                print(strategy1.perform(creature1))
                print(strategy2.perform(creature2))
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


def main() -> None:
    print("Tournament 0 (basic)")
    battle([
        (FlameFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ])
    print("\nTournament 1 (error)")
    battle([
        (FlameFactory(), AggressiveStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
    ])
    print("\nTournament 2 (multiple)")
    battle([
        (AquaFactory(), NormalStrategy()),
        (HealingCreatureFactory(), DefensiveStrategy()),
        (TransformCreatureFactory(), AggressiveStrategy()),
    ])


if __name__ == "__main__":
    main()
