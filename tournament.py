from ex0 import FlameFactory, AquaFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy, InvalidStrategyError

def battle(opponents):
    print(f"*** Tournament ***\n{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]

            creature1 = factory1.create_base()
            creature2 = factory2.create_base()

            print("\n* Battle *")
            print(f"{creature1.describe()} vs. {creature2.describe()}")
            print("now fight!")

            try:
                print(strategy1.perform(creature1))
                print(strategy2.perform(creature2))
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return

def main():
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
