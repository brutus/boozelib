from ward import each
from ward import test

from boozelib import get_degradation
from tests.fixtures import user_emma
from tests.fixtures import user_komathy
from tests.fixtures import user_paul
from tests.fixtures import user_tyrice


@test("case for `get_degradation`: {user} → {minutes}", tags=["integration"])
def _(
    user=each(user_emma, user_komathy, user_tyrice, user_paul),
    minutes=60,
    exp=each("0.191936872876", "0.250505195262", "0.188987044034", "0.217695813527"),
):
    res = get_degradation(**vars(user), minutes=minutes)
    assert isinstance(res, float)
    assert str(res).startswith(exp), f"not equal enough:\n-{res}\n+{exp}"
