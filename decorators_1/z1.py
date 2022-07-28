import functools
def decorator(func):
    @functools.wraps(func)
    def decorated():
        func()
    return decorated

@decorator
def wrapped():
    print("Hello")
wrapped()