def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if  num == 1:
        return product
    return fact_iter(num - 1, num * product)



#汉诺塔的移动：实现将A上的N个盘子借助B移动到C，函数可以打印出把N个盘子从A借助B移动到C过程
def move(n, a='A', b='B', c='C'):
    #每个过程都是靠这个n=1时输出的a-->，需要通过下面递归的方法改变a和c的值
    if n == 1:
        print (a, '-->', c)
    else:
        move(n-1, a, c, b)  #第一步：将A柱子上的前(N-1)个圆盘借助C移动到柱子B上
        move(1, a, b, c)  #第二步：将A柱子上的第N个(最大的一个)移动到C柱子上
        move(n-1, b, a, c)  #第三步：将B柱子上的(N-1)个圆盘借助A移动到柱子C上
