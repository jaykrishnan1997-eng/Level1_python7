#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   capacitor.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/21 10:12:40 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/21 11:28:55 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex1 import HealingCreatureFactory as HCF, TransformCreatureFactory as TCF


def test_healing(factory: HCF) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("Testing Creature with healing capability")
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.heal())

    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.heal())


def test_transform(factory: TCF) -> None:
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("Testing Creature with transform capability")
    print(" base:")
    print(base.describe())
    print(base.attack())
    print(base.transform())
    print(base.attack())
    print(base.revert())

    print(" evolved:")
    print(evolved.describe())
    print(evolved.attack())
    print(evolved.transform())
    print(evolved.attack())
    print(evolved.revert())


def main() -> None:
    healing = HCF()
    transform = TCF()

    test_healing(healing)
    print()
    test_transform(transform)


if __name__ == "__main__":
    main()
