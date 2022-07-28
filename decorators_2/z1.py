from functools import wraps

def decorator(func):
    @wraps(func)
    def decorated():
        func()
    return decorated

@decorator
def wrapped():
    '''Документация'''
    print('функция wrapped')
print(wrapped.__name__)
print(wrapped.__doc__)