import matplotlib.pyplot as plt  # 基本功能在分模块.pyplot并缩写成plt
import numpy as np

x = np.linspace(-3, 3, 50)
y1 = 2*x+1
y2 = x**2

##plt.figure()  # .figure(): 在figure下面的数据会显示在此figure上, figure是有顺序的, figure1、figure2...
##plt.plot(x, y1)  # .plot(x, y):x是横坐标, y是纵坐标, 把x, y展示出来

plt.figure(num=3, figsize=(8, 5))  #figure(num=编号, figsize=(长, 宽))
plt.plot(x, y2)  
# figure里可以显示多个数据, plot(x, y, color=颜色, linewidth=线宽, linestyle=样式)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')  

plt.xlim((-1, 2))
plt.ylim((-2, 3))
plt.xlabel('I am x')
plt.ylabel('I am y')

plt.show()  # plt.show(): 在脚本中运行到plt.show(), 图才会出来

