#!/usr/bin/env python3
"""
Factory pattern extending a registry
"""


class Bus:
    def mode(self) -> str:
        return "road"


class Train:
    def mode(self) -> str:
        return "rails"


class Bike:
    def mode(self) -> str:
        return "lane"


class Scooter:
    def mode(self) -> str:
        return "scooter_lane"


class VehicleFactory:
    def __init__(self):
        self._registry = {}

    def register_kind(self, name: str, cls):
        self._registry[name] = cls

    def create(self, kind: str):
        if kind not in self._registry:
            raise ValueError(f"Unknown vehicle kind: {kind}")
        return self._registry[kind]()


def main():
    factory = VehicleFactory()
    factory.register_kind("bus", Bus)
    factory.register_kind("train", Train)
    factory.register_kind("bike", Bike)

    print(factory.create("bus").mode())
    print(factory.create("train").mode())
    print(factory.create("bike").mode())

    factory.register_kind("scooter", Scooter)
    print(factory.create("scooter").mode())


if __name__ == "__main__":
    main()
