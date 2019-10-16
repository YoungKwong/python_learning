##d = {'a': 1, 'b': 2, 'c': 3}
##
###默认情况下dict迭代的是key.
##for key in d:
##    print(key)
##
###迭代value.
##for value in d.values():
##    print(value)
##
###同时迭代key和value.
##for k, v in d.items():
##    print(k, v)
##
###enumerate函数可以把一个list变成索引-元素对
##for i, value in enumerate(L):
##    print(i, value)

def findMinAndMax(L):
    if L == []:
        return (None, None)
    return (my_min(L), my_max(L))
        
def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    else:
        a = L[0]
        b = L[0]
        for num in L:
            if a > num:
                a = num
            if b < num:
                b = num
        return (a, b)
        
        


        
            
