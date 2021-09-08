from bs4 import BeautifulSoup
from urllib.request import urlopen

page1 = '''
<html>
<title>나의 홈페이지</title>
<body>
<div>
</div>
<div>
</div>
<div>
    <a href="https://www.naver.com/">naver</a>
    <a href="https://www.google.com">google</a>
    <p class="p3"> [영역1] 필요없는 정보1 </p>
    <p class="p3"> [영역1] 필요없는 정보3 </p>
    <p id="p4"> [영역1] 필요없는 정보2 </p>
</div>
<div>
    <a href="https://www.naver.com/">naver</a>
    <a href="https://www.google.com">google</a>
    <p class="p3"> [영역2] 강아지 사진과 네이버 링크 </p>
    <p class="p3"> [영역2] 강아지 사진과 네이버 링크222 </p>
    <p id="p4"> [영역2] 간단한 나의 홈페이지를 만들다.</p>
</div>
</body>
</html>
'''

#
soup1 = BeautifulSoup(page1, 'lxml')
# print( soup1.title )

# ##
# one_info = soup1.find_all("div")
# print(len(one_info) )
# print(one_info[3])

# target_info = soup1.find_all('div')[3]
# target_info = target_info.find_all('p', class_='p3')
#
# for i in target_info:
#     print(i.text)
# info = []
# target_info = soup1.find_all('p', class_='p3')
# for i in target_info[0:2]:
#     info.append(i.text)
#
# print(info)

target_info = soup1.find_all('div')[2]
print(target_info.children)
print(list(target_info.children)[9])