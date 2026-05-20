#!/usr/bin/env python3
"""
Decorator pattern - Adding a new wrapper
"""
from typing import Protocol


class Beverage(Protocol):
    def cost(self) -> int:
        ...

    def description(self) -> str:
        ...


class Coffee:
    def cost(self) -> int:
        return 50

    def description(self) -> str:
        return "Coffee"


class MilkDecorator:
    def __init__(self, inner: Beverage):
        self._inner = inner

    def cost(self) -> int:
        return self._inner.cost() + 10

    def description(self) -> str:
        return self._inner.description() + " + milk"


class SugarDecorator:
    def __init__(self, inner: Beverage):
        self._inner = inner

    def cost(self) -> int:
        return self._inner.cost() + 5

    def description(self) -> str:
        return self._inner.description() + " + sugar"


class CaramelDecorator:
    def __init__(self, inner: Beverage):
        self._inner = inner

    def cost(self) -> int:
        return self._inner.cost() + 15

    def description(self) -> str:
        return self._inner.description() + " + caramel"


def main():
    coffee = Coffee()
    
    milk_coffee = MilkDecorator(coffee)
    sugar_milk_coffee = MilkDecorator(SugarDecorator(coffee))
    caramel_combo = CaramelDecorator(MilkDecorator(SugarDecorator(coffee)))

    print(f"{milk_coffee.description()} {milk_coffee.cost()}")
    print(f"{sugar_milk_coffee.description()} {sugar_milk_coffee.cost()}")
    print(f"{caramel_combo.description()} {caramel_combo.cost()}")


if __name__ == "__main__":
    main()
