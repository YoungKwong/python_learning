def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

def triangles(num):
    L = [1]
    t = []
    for i in range(num):
        t.append(1)
        if len(L) <= 1:
            yield L 
            L.append(L[0])
        elif len(L) >1:
            yield L
            for j in range(i):
                r, s = L[j], L[j+1]
                t[j] = r + s
            L[1:i+1] = t[:i]
            L.append(L[0])
        else:
            pass
            

def my_triangles(num):
    L = [1]
    t = []
    for i in range(num):
        t.append(i)
        if len(L) <= 1:
            print(L)
            L.append(L[0])
        elif len(L) >1:
            print(L)
            for j in range(i):
                r, s = L[j], L[j+1]
                t[j] = r + s
            L[1:i+1] = t[:i]
            L.append(L[0])
        else:
            pass
            
            
            
            
            

         

        
        
    
        
