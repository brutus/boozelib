import pytest

from boozelib import get_blood_alcohol_content

from .conftest import drink_beer
from .conftest import drink_vodka
from .conftest import user_emma
from .conftest import user_paul


@pytest.mark.parametrize(
    "user,drink,exp",
    [
        (user_emma, drink_beer, "0.5971369378"),
        (user_emma, drink_vodka, "0.9749174495"),
        (user_paul, drink_beer, "0.2761707407"),
        (user_paul, drink_vodka, "0.4508910053"),
    ],
)
def test_get_blood_alcohol_content(user, drink, exp):
    res = get_blood_alcohol_content(**dict(user, **drink))
    assert isinstance(res, float)
    assert res, exp
