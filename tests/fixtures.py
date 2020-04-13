from ward import fixture

from tests.classes import Drink
from tests.classes import User


@fixture(scope="global")
def user_emma():
    return User(age=32, weight=42, height=155, sex=True)


@fixture(scope="global")
def user_komathy():
    return User(age=30, weight=80, height=173, sex=True)


@fixture(scope="global")
def user_tyrice():
    return User(age=30, weight=68, height=172, sex=False)


@fixture(scope="global")
def user_paul():
    return User(age=34, weight=103, height=186, sex=False)


@fixture(scope="global")
def drink_beer():
    return Drink(volume=500, percent=4.9)


@fixture(scope="global")
def drink_vodka():
    return Drink(volume=100, percent=40.0)
