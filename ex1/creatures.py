from .capabilities import TransformCapability, HealCapability
from ex0.creatures import Creature


class Shiftling(Creature, TransformCapability):
    def __init__(self, name, typ) -> None:
        Creature.__init__(self, name, typ)
        TransformCapability.__init__(self)

    def attack(self):
        if self._transformed:
            return "Shiftling performs a boosted strike!"
        else:
            return "Shiftling attacks normally."

    def transform(self):
        self._transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self):
        self._transformed = False
        return "Shiftling returns to normal."


class Morphagon(Creature, TransformCapability):
    def __init__(self, name, typ) -> None:
        Creature.__init__(self, name, typ)
        TransformCapability.__init__(self)

    def attack(self):
        if self._transformed:
            return "Morphagon unleashes a devastating morph strike!"
        else:
            return "Morphagon attacks normally."

    def transform(self):
        self._transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self):
        self._transformed = False
        return "Morphagon stabilizes its form."


class Sproutling(Creature, HealCapability):
    def __init__(self, name, typ) -> None:
        Creature.__init__(self, name, typ)
        HealCapability.__init__(self)

    def attack(self):
        return "Sproutling uses Vine Whip!"

    def heal(self):
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self, name, typ) -> None:
        Creature.__init__(self, name, typ)
        HealCapability.__init__(self)

    def attack(self):
        return "Bloomelle uses Petal Dance!"

    def heal(self):
        return "Bloomelle heals itself and others for a large amount"
