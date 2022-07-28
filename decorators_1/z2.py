import functools
from datetime import datetime
def decorator(func):
    @functools.wraps(func)
    def decorated(*args, **kwargs):
        start = datetime.now()
        func(a)
        stop = datetime.now()
        print(stop-start)
    return decorated

@decorator
def wrapped(a):
    print(4*a)
a = float(input('Enter side\n'))
wrapped(a)