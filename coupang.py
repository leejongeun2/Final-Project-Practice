from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus
import csv
import ssl
import requests
import re
import urllib.request



# url = 'https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
# html = urllib.request.urlopen(url).read()
# soup = BeautifulSoup(html, 'html.parser')
# print(soup)

response = urlopen('https://www.beanbrothers.co.kr/goods/goods_list.php?page={page}&cateCd=001')
soup = BeautifulSoup(response, 'html.parser')

items = soup.select('div.item_cont')
lis = []
for item in items:
    temp = []
    name = item.select_one('a > strong.item_name').text
    # price = item.select_one('li.xans-record- > div.box > div.description > div.txt > ul.xans-element- xans-product xans-product-listitem spec > li.xans-record- > strong.title displaynone').text
    temp.append(name)
    # temp.append(price)
    lis.append(temp)

# def saveToFile(filename, shop):    # 저장된 순위를 csv 파일로 저장
with open('shopping2.csv', 'w', encoding='utf-8-sig',newline='') as f:
    writer = csv.writer(f)
    writer.writerows(lis)
f.close