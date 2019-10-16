import os
os.makedirs('./img/', exist_ok=True)

IMAGE_URL = "https://ss0.baidu.com/73x1bjeh1BF3odCf/it/u=2350332598,279791532&fm=85&s=D83C67DA8270B5CE0AAC1F3C0300C054"

#方法1.urlretrieve  #Download the image url using urlretrieve
from urllib.request import urlretrieve  #载入urllib.request模块中的urlretrieve函数
#urletrieve()：第一个参数是"从哪里来"，第二个参数是"到哪里去"
urlretrieve(IMAGE_URL, './img/image2.png')

#方法2.request download  #Using requests.get to download at once
import requests
r = requests.get(IMAGE_URL)  #requests.get()拿到的网页也可以是文件的地址，拿到后存到r里面
with open('./img/image3.png', 'wb') as f:  #以写入的形式打开文件，把r.content写入文件image3.png
    f.write(r.content)

#方法3.download chunck by chunck  #Set stream = True in get() function. This is more efficient
#上面两种方法都是全部下载好放到内存去之后才可以把文件存到本地，如果文件太大，就用方法3
r = requests.get(IMAGE_URL, stream=True)  #stream=True：时时刻刻的下载
with open('./img/image4.png', 'wb') as f:
    #以每次单位大小chunk_size为32字节循环的写入(r.iter_content：就是不断循环的写入文件)
    for chunk in r.iter_content(chunk_size=32): 
        f.write(chunk)  #每次循环文件写入chunk
