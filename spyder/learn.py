# 使用request和bs4编写基本爬虫
# https://www.cnblogs.com/baojinjin/p/6819389.html
import requests
from bs4 import BeautifulSoup

res = requests.get('http://book.zongheng.com/chapter/734213/40615154.html')
res.encoding = 'utf-8'
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.encode('gb18030'))
print(soup.encode('utf-8', 'ignore'))


