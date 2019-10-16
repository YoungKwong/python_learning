#位置参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
    
#默认参数
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

#定义默认参数要牢记一点：默认参数必须指向不变对象
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

#可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n *n
    return sum

#关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

#命名关键字参数
def person1(name, age, *agrs, city, job):
    print(name, age, city, job)

#参数组合：顺序：位置参数、默认参数、可变参数、命名关键字参数、关键字参数
def f1(a, b, c=0, *args, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

#练习
def product(*args):
    sum = 1
    if args ==():
        raise TypeError('product() missing requred argument')
    else:
        for n in args:
            sum = sum * n
    return sum













