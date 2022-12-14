#!/usr/bin/env python3
# Anchor extraction from HTML document
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import quote_plus
import csv
import ssl
import requests

response = urlopen('https://search.shopping.naver.com/search/all?query=%EC%9B%90%ED%94%BC%EC%8A%A4&bt=-1&frm=NVSCVUI')
soup = BeautifulSoup(response, 'html.parser')
# shop = [ ]
# for anchor in soup.select('p.name'):
#     # shop.append(anchor.get_text())
#     print(anchor.text)

items = soup.select('li.basicList_item__0T9JD')
# items = soup.select('li.xans-record-')
lis = []
for item in items:
    temp = []
    name = item.select_one('div.basicList_title__VfX3c > a').text
    # price = item.select_one('li.xans-record- > div.box > div.description > div.txt > ul.xans-element- xans-product xans-product-listitem spec > li.xans-record- > strong.title displaynone').text
    temp.append(name)
    # temp.append(price)
    lis.append(temp)

# def saveToFile(filename, shop):    # 저장된 순위를 csv 파일로 저장
with open('shopping1.csv', 'w', encoding='utf-8-sig',newline='') as f:
    writer = csv.writer(f)
    writer.writerows(lis)
f.close

# saveToFile('shop.csv', shop)

