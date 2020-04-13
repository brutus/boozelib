from dataclasses import dataclass


@dataclass
class User:
    age: int
    weight: int
    height: int
    sex: bool


@dataclass
class Drink:
    volume: int
    percent: float
