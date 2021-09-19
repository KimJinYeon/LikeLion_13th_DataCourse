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
    + 최근 가격 상승은 암호화폐 가격 상승에 따른 것인데, 
* [다나와 상품 정보 크롤링](https://github.com/KimJinYeon/LikeLion_13th_DataCourse/blob/main/05_selenium/danawa.py)
    - [다나와 상품 정보 1페이지 csv](https://github.com/KimJinYeon/LikeLion_13th_DataCourse/blob/main/05_selenium/danawa_vga_info_p1.csv)
    - [다나와 상품 리뷰 csv](https://github.com/KimJinYeon/LikeLion_13th_DataCourse/blob/main/05_selenium/danawa_com.csv)
    - [다나와 상품 리뷰 인포그래픽](https://github.com/KimJinYeon/LikeLion_13th_DataCourse/blob/main/05_selenium/danawa_vga_wordcloud.png)
- 다나와에서 셀레니움으로 '그래픽카드'를 검색한 후, 이름, 가격, 별점, 리뷰 정보 수집
- ChromeOptions에서 add_argument('disable_gpu')를 추가하면 gpu를 사용하지 않고 실행할 수 있다. (20210912 추가)