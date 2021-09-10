#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from bs4 import BeautifulSoup


# In[2]:


driver = webdriver.Chrome('chromedriver')


# In[3]:


url = 'https://www.amazon.com/'
driver.get(url)


# In[4]:


ama_src_bar = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
ama_src_btn = driver.find_element_by_xpath('//*[@id="nav-search-submit-button"]')


# In[5]:


ama_src_bar.send_keys('computer')
ama_src_btn.click()


# In[7]:


page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')
soup.title.text


# In[8]:


cur_url = driver.current_url
cur_url


# In[14]:


tmp = soup.find_all('h2', class_='a-size-mini a-spacing-none a-color-base s-line-clamp-2')[1]
print(tmp)
print()
print(tmp.span.text)
print()
print(tmp.a.attrs['href'])


# In[25]:


'https://www.amazon.com/' + tmp.a.attrs['href']


# In[16]:


# 아마존 리뷰 가져오기
driver = webdriver.Chrome('chromedriver')

url = 'https://www.amazon.com/HP-24-inch-Computer-Processor-24-dd0010/dp/B0849GZCQR/ref=sr_1_2?dchild=1&keywords=computer&qid=1631254252&sr=8-2'
driver.get(url)


# In[19]:


first_review = driver.find_element_by_xpath('//*[@id="acrCustomerReviewText"]')
first_review.click()


# In[20]:


page = driver.page_source
soup = BeautifulSoup(page, 'lxml')
soup.title


# In[21]:


txt = soup.find_all('span', class_='a-size-base review-text review-text-content')
txt[0].text.strip()


# In[22]:


all_r = soup.find_all('span', class_='a-size-base review-text review-text-content')
all_review = []
for review in all_r:
    all_review.append(review.text.strip())
all_review


# In[24]:


import pandas as pd

dict_review = {'review': all_review}
review = pd.DataFrame(dict_review)
review.to_csv('amazon_computer_review.csv', index=False)


# In[ ]:




