from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://finance.naver.com/sise/sise_index.nhn?code=KOSPI"

page = urlopen(url)

soup = BeautifulSoup(page, 'html.parser')

KOSPI = soup.find('em', id='now_value')
quant = soup.find('td', id='quant')
high_value = soup.find('td', id='high_value')
week_high = soup.find_all('td', class_='td')[2]

news = []
tmp_news = soup.find('ul', class_='sise_report').find_all('a')
for i in tmp_news:
    news.append(i.text)

print('코스피: ', KOSPI.text)
print('코스피 거래량(천주): ', quant.text)
print('장중 최고: ', high_value.text)
print('52주 최고: ', week_high.text)
print('=====시황 뉴스=====')
for i in news:
    print(i)

# 시황뉴스 csv 파일로 만들기

import pandas as pd

dat = pd.DataFrame({'시황뉴스':news})
print(dat)
dat.to_csv("news.csv", index=False)
dat.to_excel('news_excel.xlsx', index=False)