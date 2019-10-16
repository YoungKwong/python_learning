from bs4 import BeautifulSoup  #引入模块bs4的BeautifulSoup功能，bs4是beautifulsoup的模块名
from urllib.request import urlopen
import re

html1 = urlopen(
    "https://morvanzhou.github.io/static/scraping/basic-structure.html"
    ).read().decode('utf-8')

html2 = urlopen(
    "https://morvanzhou.github.io/static/scraping/list.html"
    ).read().decode('utf-8')

html3 = urlopen(
    "https://morvanzhou.github.io/static/scraping/table.html"
    ).read().decode('utf-8')
#print(html)


#one
soup1 = BeautifulSoup(html1, features='html.parser')  #用BeautifulSoup把html喂给soup，并用'***'形式解析
print(soup1.title)
print('\n', soup1.a)

all_href = soup1.find_all('a')  #.find_all('a')：找到网页里所有的a标签并返回<a>***</a>

all_href= [l['href'] for l in all_href]  #如下面两段代码

##for l in all_href:
##    print(l['href'])  #把属性标签囊括在['']里面，返回的就是属性标签所对应的内容

print('\n', all_href)



##two
soup2 = BeautifulSoup(html2, features='html.parser')
#use class to narrow search(只find对应的class)
month = soup2.find_all('li', {'class': 'month'})  #find_all第二个参数：通过字典的形式把'class':'className'
for m in month:
    print(m.get_text())  #.get_text()：只显示所有的text，不包括html的code

jan = soup2.find('ul', {'class': 'jan'})  #find第二个参数：通过字典的形式把'class':'className'
d_jan = jan.find_all('li')  #分支里再继续find_all，就可以直接分支名.find_all
for d in d_jan:
    print(d.get_text())




##three
soup3 = BeautifulSoup(html3, features='html.parser')

#在img标签里find_all 'src'属性，用正则表达式re.compile()匹配对应的内容
img_links = soup3.find_all("img", {"src": re.compile('.*?\.jpg')})
for link in img_links:
    print(link['src'])

#在a标签里find_all 'href'属性，用正则表达式re.compile()匹配对应的内容
course_links = soup3.find_all('a', {'href': re.compile('https://.*?')})  
for link2 in course_links:
    print(link2['href'])


