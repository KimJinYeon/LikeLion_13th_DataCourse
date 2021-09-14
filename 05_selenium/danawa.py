from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import re

# 크롬 창을 띄우지 않고 실행하는 옵션
chrome_option = webdriver.ChromeOptions()
chrome_option.add_argument('headless')
chrome_option.add_argument("disable-gpu")

# 셀레니움 웹드라이버 실행
driver = webdriver.Chrome('chromedriver', options=chrome_option)
driver.implicitly_wait(5)

# 다나와 url
url_danawa = 'http://www.danawa.com/'

# 웹드라이버 실행
driver.get(url_danawa)
driver.implicitly_wait(5)

# dnw = 다나와, 검색 바와 검색 버튼 xpath 이용해서 받기
dnw_src_bar = driver.find_element_by_xpath('//*[@id="AKCSearch"]')
dnw_src_btn = driver.find_element_by_xpath('//*[@id="srchFRM_TOP"]/fieldset/div[1]/button')
driver.implicitly_wait(5)

# 셀레니움 이용해서 다나와 검색
dnw_src_bar.send_keys('그래픽 카드')
dnw_src_btn.click()
driver.implicitly_wait(5)

# 페이지 소스 받아와서 bs로 parse
page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')
driver.implicitly_wait(5)

# 제품 리스트
vga_product_list = soup.find('ul', class_='product_list').find_all('li', class_='prod_item width_change')
all_name = []
all_star = []
all_price = []
all_comment = []

for vga in vga_product_list:
    name = vga.find('div', class_='prod_info').find('a').text
    if vga.find('div', class_='point_num'):
        star = vga.find('div', class_='point_num').find('strong').text
    else:
        star = '별점없음'
    price = vga.find('div', class_='prod_pricelist').find('p', class_='price_sect').find('strong').text
    price = re.sub(',', '', price)
    all_name.append(name)
    all_star.append(star)
    all_price.append(int(price))

for vga in vga_product_list:
    vga_url = vga.find('p', class_='prod_name').find('a')['href']

    driver.implicitly_wait(5)
    driver.get(vga_url)
    driver.implicitly_wait(5)

    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    driver.implicitly_wait(5)

    cmt_list = soup.find('ul', class_='cmt_list').find_all('li')
    for cmt in cmt_list:
        comment = cmt.find('div', class_='cmt_cont').find().text
        comment = comment.replace('\n', '').replace('\t', '').replace('의견', '').replace('질문', '')
        all_comment.append(comment)

print(all_comment)
dict_comm = {'댓글': all_comment}
dict_info = {'이름': all_name, '별점': all_star, '가격': all_price}

danawa_vga = pd.DataFrame(dict_info)
danawa_vga.to_csv('danawa_vga_info_p1.csv', index=False, encoding='utf-8-sig')

danawa_com = pd.DataFrame(dict_comm)
danawa_com.to_csv('danawa_com.csv', index=False, encoding='utf-8-sig')

