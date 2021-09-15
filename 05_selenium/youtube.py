from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd


# 크롬 창을 띄우지 않고 실행하는 옵션
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument("disable-gpu")

# 셀레니움 웹드라이버 실행
driver = webdriver.Chrome('chromedriver', options=chrome_option)
driver.implicitly_wait(5)

youtube_url = 'https://www.youtube.com/watch?v=umpsXnXNkos'

driver.get(youtube_url)
driver.implicitly_wait(5)

body = driver.find_element_by_tag_name('body')
for i in range(500):
    body.send_keys(Keys.PAGE_DOWN)
    driver.implicitly_wait(5)

comments = []

for i in range(900):
    try:
        comment = driver.find_elements_by_css_selector('ytd-expander')[i].text
        print(comment)
        comments.append(comment)
    except:
        pass

dict_info = {'댓글': comments}

yt_comment = pd.DataFrame(dict_info)
yt_comment.to_csv('yt_comment.csv', index=False, encoding='utf-8-sig')