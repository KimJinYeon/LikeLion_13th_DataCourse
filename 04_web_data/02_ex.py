from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# 01 우리가 가져올 URL
# 02 내가 원하는 정보의 위치(span, id)

url = 'https://finance.naver.com/world'
page = urlopen(url)

# 구체적인 html 정보 확인하고, 구조화
soup = BeautifulSoup(page, 'html.parser')
dow = soup.find_all('dd', class_='point_status')
print(soup.title.text)
print(dow)

