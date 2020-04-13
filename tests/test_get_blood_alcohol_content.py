from ward import each
from ward import test

from boozelib import get_blood_alcohol_content
from tests.fixtures import drink_beer
from tests.fixtures import drink_vodka
from tests.fixtures import user_emma
from tests.fixtures import user_paul


@test("case for `get_blood_alcohol_content`: {user} → {drink}", tags=["integration"])
def _(
    user=each(user_emma, user_emma, user_paul, user_paul),
    drink=each(drink_beer, drink_vodka, drink_beer, drink_vodka),
    exp=each("0.5971369378", "0.9749174495", "0.2761707407", "0.4508910053"),
):
    res = get_blood_alcohol_content(**vars(user), **vars(drink))
    assert isinstance(res, float)
    assert str(res).startswith(exp), f"not equal enough:\n-{res}\n+{exp}"
