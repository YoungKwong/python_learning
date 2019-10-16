print('计算你的BMI指数')
height = float(input('请输入你的升高(单位:m):'))
weight = float(input('请输入你的体重(单位:kg):'))
bmi = weight/height**2

if bmi < 18.5:
    print('你的BMI指数是:%.2f，你的肥胖程度是:过轻(<18.5)' % bmi)
elif bmi < 25:
    print('你的BMI指数是:%.2f，你的肥胖程度是:正常(18.5-25)' % bmi)
elif bmi < 28:
    print('你的BMI指数是:%.2f，你的肥胖程度是:过重(25-28)' % bmi)
elif bmi < 32:
    print('你的BMI指数是:%.2f，你的肥胖程度是:肥胖(28-32)' % bmi)
else:
    print('你的BMI指数是:%.2f，你的肥胖程度是:过度肥胖(>32)' % bmi)
