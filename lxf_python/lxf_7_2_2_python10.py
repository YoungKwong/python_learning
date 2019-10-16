def is_palindrome(n):
    s = str(n)
    _list = []
    for i in range(len(s)//2):
        if s[i] == s[-i-1]:
            _list.append(True)
        else:
            _list.append(False)

    return all(_list[:]) == True
        
