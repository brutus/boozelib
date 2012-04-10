from nose.tools import *

from boozelib import *


# TEST DATA

f1 = User(32, 42, 155, True)
f2 = User(30, 80, 173, True)
m1 = User(30, 68, 172, False)
m2 = User(34, 103, 186, False, 'ThatGuy')

beer = Drink(500, 4.9)
shot = Drink(100, 40, 'Wodka')

test_cases_bac = (
  (f1, beer, 0.597136937838),
  (f1, shot, 0.974917449531),
  (m2, beer, 0.276170740785),
  (m2, shot, 0.450891005363),
)

test_cases_degradation = (
  (f1, 60, 0.19193687287649608),
  (f2, 60, 0.25050519526247184),
  (m1, 60, 0.1889870440348846),
  (m2, 60, 0.217695813527036),
)

test_cases_repr = (
  (f1, "<User(32, 42, 155, True, None)>"),
  (m2, "<User(34, 103, 186, False, 'ThatGuy')>"),
  (beer, "<Drink(500, 4.9, None)>"),
  (shot, "<Drink(100, 40.0, 'Wodka')>")
)

test_cases_str = (
  (f1, "[None] 32 years, 42 kg, 155 cm (female): 0"),
  (m2, "[ThatGuy] 34 years, 103 kg, 186 cm (male): 0"),
  (beer, "[None] Volumen: 500, Percent: 4.9"),
  (shot, "[Wodka] Volumen: 100, Percent: 40.0")
)

test_cases_list = (
  (f1, [32, 42, 155, True, None]),
  (m2, [34, 103, 186, False, 'ThatGuy']),
  (beer, [500, 4.9, None]),
  (shot, [100, 40.0, 'Wodka'])
)


# HELPER FUNCTIONS

def get_bac_(user, drink):
  return get_bac(
    user.age, user.weight, user.height, user.sex,
    drink.volume, drink.percent
  )

def get_degradation_(user, minutes):
  return get_degradation(
    user.age, user.weight, user.height, user.sex,
    minutes
  )

def degrade_bac_(user, bac, minutes):
  return degrade_bac(
    user.age, user.weight, user.height, user.sex,
    bac, minutes
  )


def check_get_bac(user, drink, expected):
  assert_almost_equal(get_bac_(user, drink), expected)

def check_get_degradation(user, minutes, expected):
   assert_almost_equal(get_degradation_(user, minutes), expected)

def check_degrade_bac(user, bac):
  b1 = bac - get_degradation_(user, 60)
  b2 = degrade_bac_(user, bac, 60)
  assert_almost_equal(b1, b2)

def check_repr(instance, expected):
  assert_equal(instance.__repr__(), expected)

def check_str(instance, expected):
  assert_equal(instance.__str__(), expected)

def check_as_list(instance, expected):
  assert_equal(instance.as_list(), expected)


# TESTS

def test_get_bac():
  for user, drink, expected in test_cases_bac:
    yield check_get_bac, user, drink, expected

def test_get_degradation():
  for user, minutes, expected in test_cases_degradation:
    yield check_get_degradation, user, minutes, expected

def test_degrade_bak():
  for user, drink, expected in test_cases_bac:
    yield check_degrade_bac, user, expected

def test_get_blood_alcohol():
  guy = User(26, 72, 176, False) # test person
  bac = 0 # our calculated bac (with the tested functions)
  #drink a beer
  fbac = get_blood_alcohol(guy, beer)
  bac += get_bac_(guy, beer)
  assert_almost_equal(fbac, bac)
  # wait 30 minutes
  fbac = get_blood_alcohol(guy, None, 30, fbac)
  bac -= get_degradation_(guy, 30)
  assert_almost_equal(fbac, bac)
  # now drink another in 10 minutes
  fbac = get_blood_alcohol(guy, beer, 10, fbac)
  bac += get_bac_(guy, beer)
  bac -= get_degradation_(guy, 10)
  assert_almost_equal(fbac, bac)

def test_User():
  guy = User(26, 72, 176, False) # test person
  bac = 0 # our calculated bac (with the tested functions)
  # drink a beer
  guy.drink(beer)
  bac += get_bac_(guy, beer)
  assert_almost_equal(guy.bac, bac)
  # wait 30 minutes
  guy.wait(30)
  bac -= get_degradation_(guy, 30)
  assert_almost_equal(guy.bac, bac)
  # now drink another in 10 minutes
  guy.drink(beer, 10)
  bac += get_bac_(guy, beer)
  bac -= get_degradation_(guy, 10)
  assert_almost_equal(guy.bac, bac)

def test_repr():
  for ins, expected in test_cases_repr:
    yield check_repr, ins, expected

def test_str():
  for ins, expected in test_cases_str:
    yield check_str, ins, expected

def test_as_list():
  for ins, expected in test_cases_list:
    yield check_as_list, ins, expected

