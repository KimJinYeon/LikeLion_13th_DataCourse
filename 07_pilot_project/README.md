# LikeLion_13th_DataCourse
파일럿 프로젝트: 다나와에서 그래픽카드 정보 수집

***
### 개요
* 다나와에서 그래픽카드를 검색한 후, 상위 검색결과 40개에 대해 이름, 별점, 가격 수집
* 수집한 40개의 결과에 대해 개당 16개씩 상품 리뷰 수집
* 수집한 리뷰는 빈도 기반 인포그래픽으로 제작

### 목적
* 최신 그래픽 카드의 가격대 파악
* 최근 그래픽 카드 가격의 상승에 대한 소비자들의 반응 파악
* 인포그래픽이 소비자 리뷰에 대한 좋은 시각적 자료가 될 수 있을지 파악

### 데이터 수집 전략
* selenium, BeautifulSoup, worlcloud 라이브러리 이용

### 결과 예측
* 그래픽 카드의 가격대는 100만원 내외로 매우 높을 것으로 예상
* 최근 그래픽 카드의 가격 상승에 대해서 소비자들은 매우 불쾌해할 것으로 예상
    + 최근 가격 상승은 암호화폐 가격 상승에 따른 것인데, 이를 반기지 않는 소비자가 많다.
    + 인포그래픽에도 코인, 떡상과 같은 키워드가 존재하지 않을까?

### 결과
* [다나와 상품 정보 크롤링](https://github.com/KimJinYeon/LikeLion_13th_DataCourse/blob/main/05_selenium/danawa.py)
    - [다나와 상품 정보 1페이지 csv](https://github.com/KimJinYeon/LikeLion_13th_DataCourse/blob/main/05_selenium/danawa_vga_info_p1.csv)
    - [다나와 상품 리뷰 csv](https://github.com/KimJinYeon/LikeLion_13th_DataCourse/blob/main/05_selenium/danawa_com.csv)
    - [다나와 상품 리뷰 인포그래픽](https://github.com/KimJinYeon/LikeLion_13th_DataCourse/blob/main/05_selenium/danawa_vga_wordcloud.png)
* 그래픽 카드의 가격대는 100만원 내외로 매우 높았고 300만원대 고가의 제품도 있었다.
* 리뷰에 고객문의에 대한 답변이 매우 많아서, 인포그래픽에서 유의미한 정보를 얻을 수 없었다.

### 프로젝트를 하며 알게된 점
- selenium에서 ChromeOptions를 이용한 브라우저 조작
    + ChromeOptions에서 add_argument('headless')를 추가하면 브라우저 창을 키지 않고 실행할 수 있다.
    + ChromeOptions에서 add_argument('disable_gpu')를 추가하면 gpu를 사용하지 않고 실행할 수 있다.
- BeautifulSoup는 찾는 요소가 없을 경우 NoneType을 반환
    + 파이썬에서 None은 False로 취급하므로, if문의 조건에 BeautifulSoup의 find문을 넣으면 없는 요소에 대한 처리가 깔끔하게 가능하다.
- 인코딩 방식
    + 한글이 깨지는 문제는 encoding을 'utf-8-sig'로 함으로써 해결가능하다.
    + utf-8은 유니코드 8 방식을, sig는 시그니처를 의미한다.
    + 파일 맨 앞에 16진법으로 utf-8임을 명시함으로써, 이 방식으로 디코딩하게 한다.
