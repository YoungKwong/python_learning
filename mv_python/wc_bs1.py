from urllib.request import urlopen  #导入urllib.request库里面的urlopen功能
import re  #导入正则表达式模块


html = urlopen(  #urlopen()：打开一个网页链接url
    "https://space.bilibili.com/243821484?from=search&seid=14879710294690762847"
    ).read().decode('utf-8')  #read()：把网页的内容全部读出来  #if has Chinese，apply decode()
                                           #decode('utf-8')：用utf-8的形式解析中文的网页才能读取
#print(html)

res = re.findall(r"<title>(.*?)</title>", html)
print("\nPage title is:", res[0])

res2 = re.findall(r"content(.*?)>", html)
print("\nAll content:", res2)

res3 = re.findall(r"src=(.*?)>", html)
print("\nAll src:", res3)
