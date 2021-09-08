from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv

# url 정보

# tag, id, class 정보

url = 'https://movie.naver.com/movie/running/current.naver?order=reserve'

page = urlopen(url)

soup = BeautifulSoup(page, 'html.parser')

titleList = []
title = soup.find_all('dt', class_='tit')
for i in title:
    titleList.append(i.find('a').text)

ratingList = []
rating = soup.find_all('dl', class_='info_star')
for i in rating:
    ratingList.append(i.find('span', class_='num').text)

bookRateList = []
book = soup.find_all('dd', class_='star')
for i in book:
    if i.find('dl', class_='info_exp'):
        bookRateList.append(i.find('dl', class_='info_exp').find('span', class_='num').text + '%')
    else:
        bookRateList.append('예매율 없음')

peopleList = []
people = soup.find_all('span', class_='num2')
for i in people:
    peopleList.append(i.find('em').text.replace(',',''))

print(len(titleList), len(ratingList), len(bookRateList), len(peopleList))

f = open('movie.csv', 'w', newline='', encoding='UTF-8')
wr = csv.writer(f)

for i in range(len(titleList)):
    wr.writerow([titleList[i], ratingList[i], peopleList[i], bookRateList[i]])

f.close()