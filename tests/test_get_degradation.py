import pytest

from boozelib import get_degradation

from .conftest import user_emma
from .conftest import user_komathy
from .conftest import user_paul
from .conftest import user_tyrice


@pytest.mark.parametrize(
    "user,minutes,exp",
    [
        (user_emma, 60, "0.191936872876"),
        (user_komathy, 60, "0.250505195262"),
        (user_tyrice, 60, "0.188987044034"),
        (user_paul, 60, "0.217695813527"),
    ],
)
def test_get_degradation(user, minutes, exp):
    res = get_degradation(minutes=minutes, **user)
    assert isinstance(res, float)
    assert res, exp
