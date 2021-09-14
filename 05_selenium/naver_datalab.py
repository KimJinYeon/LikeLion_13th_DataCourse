from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('headless')
chrome_option.add_argument('disable-gpu')

naver_datalab_url = 'https://datalab.naver.com/'

driver = webdriver.Chrome('chromedriver', options=chrome_option)

driver.get(naver_datalab_url)

all_day = []
all_pop_word = []

for i in range(12, 0, -1):
    print(f'{i}번쨰 날')
    if i%2:
        time.sleep(5)
    else:
        time.sleep(4)
    div_xpath = '//*[@id="content"]/div[1]/div[4]/div/div[1]/div/div/div[' + str(i) + ']/div'
    day_div = driver.find_element_by_xpath(div_xpath)
    print(day_div.find_element_by_css_selector('div strong span').text)
    all_day.append(day_div.find_element_by_css_selector('div strong span').text)
    day_pop_word = []
    for j in range(10, 0, -1):
        print(f'{j}번째 검색어')
        if i % 2:
            time.sleep(2)
        else:
            time.sleep(3)
        word_xpath = div_xpath + '/div/ul/li[' + str(j) + ']/a/span'
        pop_word = driver.find_element_by_xpath(word_xpath).text
        print(pop_word)
        day_pop_word.append(pop_word)
    all_pop_word.append(day_pop_word)

print(all_day)
print(all_pop_word)

dict_info = {'날짜' : all_day, '인기검색어': all_pop_word}

naver_datalab = pd.DataFrame(dict_info)
naver_datalab.to_csv('naver_datalab_pop_word.csv', index=False, encoding='utf-8-sig')