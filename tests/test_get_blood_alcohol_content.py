import ward

from boozelib import get_blood_alcohol_content
from tests.data import drink_beer
from tests.data import drink_vodka
from tests.data import user_emma
from tests.data import user_paul


cases = [
    # user, drink, expected BAC raise
    (user_emma, drink_beer, "0.5971369378"),
    (user_emma, drink_vodka, "0.9749174495"),
    (user_paul, drink_beer, "0.2761707407"),
    (user_paul, drink_vodka, "0.4508910053"),
]

users, drinks, exps = zip(*cases)


@ward.test("`get_blood_alcohol_content` for *user* and *drink*")
def _(user=ward.each(*users), drink=ward.each(*drinks), exp=ward.each(*exps)):
    res = get_blood_alcohol_content(**dict(user, **drink))
    assert isinstance(res, float)
    assert str(res).startswith(exp), f"not equal enough:\n-{res}\n+{exp}"
