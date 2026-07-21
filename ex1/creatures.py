#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   creatures.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/21 10:12:55 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/21 10:46:38 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from .capabilities import TransformCapability, HealCapability
from ex0.creatures import Creature


class Shiftling(Creature, TransformCapability):
    def __init__(self, name: str, typ: str) -> None:
        Creature.__init__(self, name, typ)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self._transformed:
            return "Shiftling performs a boosted strike!"
        else:
            return "Shiftling attacks normally."

    def transform(self) -> str:
        self._transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        self._transformed = False
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self, name: str, typ: str) -> None:
        Creature.__init__(self, name, typ)
        TransformCapability.__init__(self)

    def attack(self) -> str:
        if self._transformed:
            return "Morphagon unleashes a devastating morph strike!"
        else:
            return "Morphagon attacks normally."

    def transform(self) -> str:
        self._transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        self._transformed = False
        return "Morphagon stabilizes its form."


class Sproutling(Creature, HealCapability):
    def __init__(self, name: str, typ: str) -> None:
        Creature.__init__(self, name, typ)
        HealCapability.__init__(self)

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self) -> str:
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self, name: str, typ: str) -> None:
        Creature.__init__(self, name, typ)
        HealCapability.__init__(self)

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self) -> str:
        return "Bloomelle heals itself and others for a large amount"
