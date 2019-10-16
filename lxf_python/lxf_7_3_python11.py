def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

def count():
    fs = []
    for i in range(1,4):
        def f():
            return i * i
        fs.append(f())
    return fs

def createCounter():
    def c():
        i = 0
        while True:
            i = i + 1
            yield i
    f = c()
    def counter():
        return next(f)
    return counter

def my_createCounter():
    pass
    
