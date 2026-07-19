from abc import ABC, abstractmethod


class Creature(ABC):
    def __init__(self, name, typ) -> None:
        self._name = name
        self._typ = typ

    @abstractmethod
    def attack(self) -> None:
        pass

    def describe(self) -> str:
        return f"{self._name} is a {self._typ} type Creature"


class Flameling(Creature):
    def __init__(self, name: str, typ: str) -> None:
        self._name = name
        self._typ = typ

    def attack(self) -> str:
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    def __init__(self, name: str, typ: str) -> None:
        self._name = name
        self._typ = typ

    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self, name: str, typ: str) -> None:
        self._name = name
        self._typ = typ

    def attack(self) -> str:
        return "Aquabub uses Water Gun!"


class Torragon(Creature):
    def __init__(self, name: str, typ: str) -> None:
        self._name = name
        self._typ = typ

    def attack(self) -> str:
        return "Torragon uses Hydro Pump!"
