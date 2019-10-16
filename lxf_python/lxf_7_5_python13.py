import functools
import time

def throughout(*args1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            try:
                print('begin call', *args1)
                return func(*args, **kw)
            except:
                pass
            finally:
                print('end call', *args1)
        return wrapper
    return decorator

def be(func):
    def wrapper(*args, **kw):
        print('begin call')
        fn = func()
        print('end call')
        return fn
    return wrapper

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        try:
            rtb = time.time()
            return fn(*args, **kw)
        except:
            pass
        finally:
            rte = time.time()
            print('%s executed in %s ms' % (fn.__name__, rte - rtb))
    return wrapper

def log2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@throughout('text')
def now():
    print('2019-10-08')
