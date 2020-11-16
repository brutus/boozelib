import ward


@ward.fixture(scope="global")
def user_emma():
    return dict(age=32, weight=42, height=155, sex=True)


@ward.fixture(scope="global")
def user_komathy():
    return dict(age=30, weight=80, height=173, sex=True)


@ward.fixture(scope="global")
def user_tyrice():
    return dict(age=30, weight=68, height=172, sex=False)


@ward.fixture(scope="global")
def user_paul():
    return dict(age=34, weight=103, height=186, sex=False)


@ward.fixture(scope="global")
def drink_beer():
    return dict(volume=500, percent=4.9)


@ward.fixture(scope="global")
def drink_vodka():
    return dict(volume=100, percent=40.0)
