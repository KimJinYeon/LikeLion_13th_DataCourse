# 지수 정보 20210908_14_index.csv
# 시황정보 뉴스 20210908_14_news.csv
# 시황정보 리포트 20210908_14_report.csv
# 인기검색어 20210908_14_pop_word.csv
# 가장 많이 본 뉴스 20210908_14_cnt_news.csv

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

url = 'https://finance.naver.com/sise/sise_index.nhn?code=KOSDAQ'
page = urlopen(url)

soup = BeautifulSoup(page, 'html.parser')

#코스닥 지수
def kosdaq(soup:BeautifulSoup):
    subtop_sise_detail = soup.find('div', class_='subtop_sise_detail')

    subtop_sise_detail = list(subtop_sise_detail.text.split('\n'))

    while '' in subtop_sise_detail:
        subtop_sise_detail.remove('')

    index = pd.DataFrame({'코스피 주요 지수': subtop_sise_detail})
    index.to_csv("20210908_14_index.csv", index=False)

# 시황정보 뉴스
newsList = []
news = soup.find_all('ul', class_='sise_report')
news1 = news[0].find_all('a')

for i in news1:
    newsList.append(i.text)

news_data = pd.DataFrame({'시황정보 뉴스': newsList})
news_data.to_csv('20210908_14_news.csv', index=False)

# 시황정보 리포트
newsReport = []
news2 = news[1].find_all('a')

for i in news2:
    newsReport.append(i.text)

report_data = pd.DataFrame({'시황정보 리포트': newsReport})
report_data.to_csv('20210908_14_report.csv', index=False)

# 인기검색어
popList = []
pop = soup.find('table', class_='type_r1')
pop = pop.find_all('a')

for i in pop:
    popList.append(i.text)

pop_data = pd.DataFrame({'인기검색어':popList})
pop_data.to_csv('20210908_14_pop_word.csv', index=False)

# 가장 많이 본 뉴스

recent_news_list = []
recent_news = soup.find('ul', class_='right_list_1_2')
recent_news = recent_news.find_all('a')

for i in recent_news:
    recent_news_list.append(i.text)

recent_data = pd.DataFrame({'가장 많이 본 뉴스':recent_news_list})
recent_data.to_csv('20210908_14_cnt_news.csv', index=False)
