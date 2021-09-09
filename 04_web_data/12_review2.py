from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd
import time

comment = []
url = 'https://movie.naver.com/movie/point/af/list.naver?st=mcode&sword=201073&target='

for i in range(1, 34):
    if i == 1:
        modifiedUrl = url
    else:
        modifiedUrl = url + '&page=' + f'{i}'
    page = urlopen(modifiedUrl)
    soup = BeautifulSoup(page, 'lxml')

    list_netizen = soup.find('table', class_='list_netizen').find_all('td', class_='title')
    for j in list_netizen:
        dat = list(j.children)[6]
        dat = dat.strip()
        if dat != "":
            comment.append(dat)

    print(f'{i}페이지 완료')


dict_dat = {"영화댓글":comment}
dat = pd.DataFrame(dict_dat)
dat.to_csv("코다댓글.csv", index=False)
dat.to_excel("코다댓글.xlsx", index=False)
