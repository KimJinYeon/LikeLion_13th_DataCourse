from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# 셀레니움 웹드라이버 실행
driver = webdriver.Chrome('chromedriver')

# 아마존 url로 get
ama_url = 'https://www.amazon.com/'
driver.get(ama_url)

# 검색 바와 버튼 xpath로 연결
ama_src_bar = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
ama_src_btn = driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]')

# computer 검색
ama_src_bar.send_keys('computer')
ama_src_btn.click()

# computer 검색한 후 페이지 정보 받아와서 BeautifulSoup로 parse
page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')

dict_review = {}

product_list_on_page = soup.find_all('h2', class_='a-size-mini a-spacing-none a-color-base s-line-clamp-2')

for product in product_list_on_page:

    target_url = ama_url + product.a.attrs['href']

    # 아마존 리뷰 가져오기
    driver = webdriver.Chrome('chromedriver')
    driver.get(target_url)

    first_review = driver.find_element_by_xpath('//*[@id="acrCustomerReviewText"]')
    first_review.click()

    page = driver.page_source
    soup = BeautifulSoup(page, 'lxml')

    all_r = soup.find_all('span', class_='a-size-base review-text review-text-content')
    all_review = []
    for review in all_r:
        all_review.append(review.text.strip())

    print(all_review)


#
# review = pd.DataFrame(dict_review)
# review.to_csv('amazon_computer_review.csv', index=False, encoding='utf-8-sig')
