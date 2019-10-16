from bs4 import BeautifulSoup
import requests
import os

url = "http://job.jluzh.com/unijob/index.php/web/Index/jobfair-list"  

html = requests.get(url).text
soup = BeautifulSoup(html, features='html.parser')
img_a = soup.find_all('a', {"class": "card content-block mg-t-20"})
#print(len(img_ul))

os.makedirs('./img/', exist_ok=True)  #创建一个存放image的文件夹

for a in img_a:
    imgs = a.find_all('img')
    for img in imgs:
        url = img['src']  #把img标签里src的链接提取出来放到url
        r = requests.get(url, stream=True)
        image_name = url.split('/')[-1]  #命名方式
        with open('./img/%s'%image_name, 'wb') as f:  #把将要下载的文件装载到f
            for chunk in r.iter_content(chunk_size=128):
                #以每次单位大小chunk_size为32字节循环的写入(r.iter_content：就是不断循环的写入f)
                f.write(chunk)  
            print('Saved %s' % image_name)


