#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   factories.py                                         :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/07/21 10:13:04 by jkrishna            #+#    #+#            #
#   Updated: 2026/07/21 10:13:05 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from abc import ABC, abstractmethod
from .creatures import Creature, Flameling, Pyrodon, Aquabub, Torragon


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Flameling:
        f = Flameling("Flameling", "Fire")
        return f

    def create_evolved(self) -> Pyrodon:
        p = Pyrodon("Pyrodon", "Fire/Flying")
        return p


class AquaFactory(CreatureFactory):
    def create_base(self) -> Aquabub:
        a = Aquabub("Aquabub", "Water")
        return a

    def create_evolved(self) -> Torragon:
        t = Torragon("Torragon", "Water")
        return t
