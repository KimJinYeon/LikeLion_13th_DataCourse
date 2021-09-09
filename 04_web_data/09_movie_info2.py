from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd

url = 'https://movie.naver.com/movie/running/current.naver?order=reserve'
page = urlopen(url)

soup = BeautifulSoup(page, 'lxml')

movie_ul = soup.find('ul', class_='lst_detail_t1').find_all('li')

all_title = []
all_score = []
all_people = []
all_book = []
all_category = []
all_director = []
all_star = []
all_running_time = []
all_release_date = []

for movie in movie_ul:
    all_title.append(movie.find('dt', class_='tit').a.text)
    all_score.append(movie.find('span', class_='num').text)
    all_people.append(movie.find('em').text)
    if movie.find('dl', class_='info_exp'):
        all_book.append(movie.find('dl', class_='info_exp').span.text + '%')
    else:
        all_book.append("예매 정보 없음")

    info = movie.find('dl', class_='info_txt1').find_all('span', class_='link_txt')

    time = movie.find('dl', class_='info_txt1').text
    time = time.replace('\r', '')
    time = time.replace('\t', '')
    time = time.split('\n')

    while '' in time:
        time.remove('')

    running_time = ''
    release_date = ''
    cnt = 0
    for i in range(len(time)):
        if time[i] == '|':
            if cnt == 0:
                if len(time[i+1]) > 5:
                    release_date = time[i+1]
                    running_time = '상영 시간 미공개'
                    break
                running_time = time[i+1]
                cnt += 1
                continue
            if cnt == 1:
                release_date = time[i+1]
                break

    release_date = release_date[0:10]

    all_running_time.append(running_time)
    all_release_date.append(release_date)

    category_info = ''
    for category in info[0].find_all('a'):
        category_info += category.text
        category_info += ','
    category_info = category_info[:-1]

    all_category.append(category_info)

    director_info = ''
    for director in info[1].find_all('a'):
        director_info += director.text
        director_info += ','
    director_info = director_info[:-1]

    all_director.append(director_info)

    star_info = ''
    if len(info) > 2:
        for star in info[2].find_all('a'):
            star_info += star.text
            star_info += ','
        star_info = star_info[:-1]
        all_star.append(star_info)
    else:
        star_info = '출연 배우 없음'
        all_star.append(star_info)


dat_dict = {
    "제목":all_title, "평점":all_score, "참여명수":all_people,
    "예매율":all_book, "개요":all_category, "감독":all_director,
    "배우":all_star , "상영 시간":all_running_time, "개봉일":all_release_date}
dat = pd.DataFrame(dat_dict)
dat.to_csv("네이버영화.csv", index=False)
dat.to_excel("네이버영화.xlsx", index=False)