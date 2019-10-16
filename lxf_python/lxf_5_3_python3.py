import math

def quadratic():
    print('ax**2 + bx + c = 0')
    a = int(input('a:'))
    b = int(input('b:'))
    c = int(input('c:'))
    x1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
    return x1, x2
