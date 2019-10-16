def trim(s):
    i = 0
    j = 0
    n = None
    for x in range(len(s)):
        if s[i] == ' ' or s[-1 -j] == ' ': #判断第一位和最后一位是否为空格
            if s[i] == ' ' and s[-1 -j] == ' ': #如果都为空格
                i = i + 1
                j = j + 1
                n = -j
                continue
            elif s[i] == ' ':
                i = i + 1
                continue
            else:
                j = j + 1
                n = -j
                continue
        else:
            return s[i:n]
    s = ''
    return s

def trim_1(s):
    if s[:1] == " ":
        return trim(s[1:])
    elif s[-1:] == " ":
        return trim(s[:-1])
    return s
        
                
        
            
