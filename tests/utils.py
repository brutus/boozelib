from contextlib import contextmanager

import boozelib


@contextmanager
def global_degradation(value):
    org_degradation = boozelib.ALCOHOL_DEGRADATION
    try:
        boozelib.ALCOHOL_DEGRADATION = value
        yield value
    finally:
        boozelib.ALCOHOL_DEGRADATION = org_degradation
