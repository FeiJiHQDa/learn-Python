import functools

def log_one(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


def log_decorator(text=''):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


# now = log(now)
# @log_one
@log_decorator("nex")
def now():
    print("2018-10-10")

 # no now, is wrapper
print(now.__name__)


now()
# print(now.__name__)
