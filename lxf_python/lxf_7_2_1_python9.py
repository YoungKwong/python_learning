from functools import reduce

def normalize(name):
    i = 0
    s = ''
    for names in name:
        if i == 0:
            i = i + 1
            if ord(names) >= 97: 
                s = s + chr(ord(names) - 32)
            else:
                s= s + names
        else:
            if ord(names) < 97:
                s= s + chr(ord(names) + 32)
            else:
                s= s+ names
    return s

def prod(L):
    def mult(x, y):
        return x * y
    return reduce(mult, L)
                
def str2float(s):
    ans = 0
    j = 0
    _list = []
    def char2num(s):
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '.':None}
        return digits[s]
    def fn(x, y):
        return x*10 + y
    r = map(char2num, s)
    for i in list(r):
        if i != None:
            _list.append(i)
            j = j + 1
        else:
            j = 0
    ans = reduce(fn, _list)
    return ans * 10**-j
    
            
            
        
        
    #return reduce(fn, map(char2num, s))
    
