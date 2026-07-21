#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   battle.py                                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/21 10:12:43 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/21 10:59:06 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex0 import FlameFactory, AquaFactory
from ex0.factories import CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    evolved = factory.create_evolved()

    print(base.describe())
    print(base.attack())

    print(evolved.describe())
    print(evolved.attack())


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("Testing battle")
    c1 = factory1.create_base()
    c2 = factory2.create_base()

    print(f"{c1.describe()}\n vs.\n{c2.describe()}")
    print(" fight!")
    print(c1.attack())
    print(c2.attack())


def main() -> None:
    ff = FlameFactory()
    af = AquaFactory()

    for factory in (ff, af):
        test_factory(factory)
        print()

    battle(ff, af)


if __name__ == "__main__":
    main()
