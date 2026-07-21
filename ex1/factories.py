#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   factories.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/21 10:12:52 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/21 11:25:03 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from ex0.factories import CreatureFactory
from .creatures import Sproutling, Bloomelle, Shiftling, Morphagon


class HealingCreatureFactory(CreatureFactory):
    label = "Healing"

    def create_base(self) -> Sproutling:
        s = Sproutling("Sproutling", "Grass")
        return s

    def create_evolved(self) -> Bloomelle:
        b = Bloomelle("Bloomelle", "Grass/Fairy")
        return b


class TransformCreatureFactory(CreatureFactory):
    label = "Transform"

    def create_base(self) -> Shiftling:
        s = Shiftling("Shiftling", "Normal")
        return s

    def create_evolved(self) -> Morphagon:
        m = Morphagon("Morphagon", "Normal/Dragon")
        return m
