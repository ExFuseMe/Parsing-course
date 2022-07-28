import functools
from datetime import datetime
def decorator(func):
    @functools.wraps(func)
    def decorated(*args, **kwargs):
        start = datetime.now()
        func(a, b)
        stop = datetime.now()
        print(stop-start)
    return decorated

@decorator
def wrapped(a, b):
    print(a*b)
a = float(input())
b = float(input())
wrapped(a,b)