print('计算去年到今年你成绩提升 or 下降的百分点')

name = input('请输入你的名字:')

s1 = float(input('请输入你去年的成绩:'))
s2 = float(input('请输入你今年年的成绩:'))

if s2>s1:
    r = (s2-s1)/s1 *100
    print('Hi! %s, 你成绩提升了%.1f %%' % (name, r))
elif s2<s1:
    r = (s1-s2)/s1 *100
    print('Hi! %s, 你成绩下降了%.1f %%' % (name, r))
else:
    print('Hi! %s, 你的成绩没有提升也没有下降')
