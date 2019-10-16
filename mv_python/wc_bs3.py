from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random  #random：随机选取需要用到的模块

base_url = "https://baike.baidu.com"
his = ["/item/%E6%9E%97%E5%BF%97%E7%8E%B2/172898"]

for i in range(20):  #循环20次
    url = base_url + his[-1]  #把变量base_url和变量his的最后一位赋值给url

    html = urlopen(url).read().decode('utf-8')  #打开url对应的网址全部读出来('utf-8'解析中文网页)
    soup = BeautifulSoup(html, features='html.parser')  #用BeautifulSoup把html喂给soup,并解析
    print(soup.find('h1').get_text(), '        url:', his[-1])  #print第一个<h1>标签里面的text和his[-1]
    
    #1.找网页里所有的链接，打开浏览器按f12查看源代码找规律，发现所有的链接的在标签<a>里
    #2. target="_blank"意思是另外打开一个网页，"href="里面的是百度百科内的链接
    #3.找到规律用正则表达式匹配掉不符合的内容

    #find_all所有a标签里'target'对应的内容和'href'里面符合正则表达式re.compile匹配的内容
    sub_urls = soup.find_all("a", {"target": "_blank", "href": re.compile("/item/(%\w{2})+/\d+$")})

    if len(sub_urls) != 0:  #如果返回的值不是空的话，就在sub_urls里随机抽取一个"href"添加到his
        his.append(random.sample(sub_urls, 1)[0]['href'])
    else:  #返回是空的话删除his最后一个元素
        his.pop()



##url = base_url + his[-1]
##
##html = urlopen(url).read().decode('utf-8')
##soup = BeautifulSoup(html, features='html.parser')
##print(soup.find('h1').get_text(), '        url:', his[-1])
##
##sub_urls = soup.find_all("a", {"target": "_blank", "href": re.compile("/item/(%\w{2})+$")})
##print(sub_urls)
##if len(sub_urls) != 0:
##    his.append(random.sample(sub_urls, 1)[0]['href'])
##else:
##    his.pop()
##print(his)

    

