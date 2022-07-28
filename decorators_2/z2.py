import functools, time
def decorator(func):
    @functools.wraps(func)
    def decorated():
        func()
        time.sleep(3)
        print('Bye')
    return decorated

@decorator
def wrapped():
    print('Hello')
wrapped()