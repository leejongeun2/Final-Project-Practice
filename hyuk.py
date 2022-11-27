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

response = urlopen('https://www.xexymix.com/shop/shopbrand.html?xcode=005&type=X')
soup = BeautifulSoup(response, 'html.parser')

items = soup.select('dl.item-list')
lis = []
for item in items:
    temp = []
    name = item.select_one('ul > li.prd-name').text
    price = item.select_one('div.priceBox > li').text
    img = item.select_one('a > img')["src"]
    temp.append(name)
    temp.append(price) 
    temp.append(img)
    lis.append(temp)

# def saveToFile(filename, shop):    # 저장된 순위를 csv 파일로 저장
with open('shopping3.csv', 'w', encoding='utf-8-sig',newline='') as f:
    writer = csv.writer(f)
    writer.writerows(lis)
f.close