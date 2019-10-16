import requests  #载入requests模块
import webbrowser  #python自带的模块

#1.requests get 请求
param = {"wd": "莫烦python"}
#requests.get()第一个参数是.get()主要的url，后面的参数params是把键值对和前面的url组合在一起
r1 = requests.get('https://www.baidu.com/s', params=param)
print(r1.url)
webbrowser.open(r1.url)  #webrowser.open()：自动用默认的浏览器打开()里面的链接
print('1.requests get 请求\n')

#get和post的区别：get返回的url会有你提交的信息，post返回的url不会显示你提交的信息

#2.requests post 请求
data = {'firstname': '莫烦', 'lastname': '周'}
#request.post()第一个参数里面的链接是post过去后的链接，后面data是你先要提交的数据data
r2 = requests.post(
    'https://pythonscraping.com/pages/files/processing.php',
    data=data)
#将返回的值赋值给r,再输出返回的结果
print(r2.text)
print('2.requests post 请求\n')

#3.用post上传图片
file = {'uploadFile': open('./img/image1.png', 'rb')}  #以只读的形式打开路径下的img
r3 = requests.post(
    'https://pythonscraping.com/pages/files/processing2.php',
    files=file)  #requests.post()post图片后面的参数是files
print(r3.text)
print('3.用post上传图片\n')

#4.用post登录
payload = {'username': 'Morvan', 'password': 'password'}
r4 = requests.post(
    'https://pythonscraping.com/pages/cookies/welcome.php',
    data=payload)
#post是一个登录的状况(连续的)，python每一次发收请求是独立的(不连续)，是不能处理连续状况
#用post登录以后会生成一个cookies(处理连续状况)，使用cookies放在下一次登录的指令里面(变连续)
print(r4.cookies.get_dict())
r4 = requests.get(
    'http://pythonscraping.com/pages/cookies/profile.php',
    #cookies=r4.cookies
)
print(r4.text)
print('4.用post登录\n')

#5.用一连串的session(会话)控制cookies的传递
session = requests.Session()  #用requests搭建一个Session并赋值给seccion
payload = {'username': 'Morvan', 'password': 'password'}
r5 = session.post(  #直接使用session来进行post操作登录网站
    'https://pythonscraping.com/pages/cookies/welcome.php',
    data=payload)
print(r5.cookies.get_dict())
r5 = session.get(  #此时session已经包含了cookies的信息
    'http://pythonscraping.com/pages/cookies/profile.php',
)
print(r5.text)
print('5.用一连串的session(会话)控制cookies的传递\n')



















