import ward

from boozelib import get_blood_alcohol_degradation
from tests.data import user_emma
from tests.data import user_komathy
from tests.data import user_paul
from tests.data import user_tyrice
from tests.utils import global_degradation


cases = [
    # user, minutes, expected BAC degradation
    (user_emma, 60, "0.191936872876"),
    (user_komathy, 60, "0.250505195262"),
    (user_tyrice, 60, "0.188987044034"),
    (user_paul, 60, "0.217695813527"),
]

users, minutes, exps = zip(*cases)


@ward.test("`get_blood_alcohol_degradation` for *user* and *drink*")
def _(user=ward.each(*users), minutes=ward.each(*minutes), exp=ward.each(*exps)):
    res = get_blood_alcohol_degradation(minutes=minutes, **user)
    assert isinstance(res, float)
    assert str(res).startswith(exp), f"not equal enough:\n-{res}\n+{exp}"


@ward.test("`get_alcohol_degradation` with degradation set to {degradation} by call")
def _(minutes=60, degradation=0.002, user=user_emma, exp="0.15354949830119685"):
    res = get_blood_alcohol_degradation(
        minutes=minutes, degradation=degradation, **user
    )
    assert isinstance(res, float)
    assert str(res).startswith(exp), f"not equal enough:\n-{res}\n+{exp}"


@ward.test("`get_alcohol_degradation` with degradation set to {degradation} globally")
def _(minutes=60, degradation=0.002, user=user_emma, exp="0.15354949830119685"):
    with global_degradation(degradation):
        res = get_blood_alcohol_degradation(minutes=minutes, **user)
        assert isinstance(res, float)
        assert str(res).startswith(exp), f"not equal enough:\n-{res}\n+{exp}"
