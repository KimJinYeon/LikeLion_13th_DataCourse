# LikeLion_13th_DataCourse
멋쟁이 사자처럼 13회차 프로젝트 정리 및 발표

***

### 웹의 이해 및 HTML 기본 실습
  #### HTML 기본 실습
  * [title tag](https://github.com/KimJinYeon/LikeLion_13th_DataCourse/blob/main/01_web_html/01_html_title.html)
  * [body, p tag](https://github.com/KimJinYeon/LikeLion_13th_DataCourse/blob/main/01_web_html/02_html_body.html)
  * [a, img tag](https://github.com/KimJinYeon/LikeLion_13th_DataCourse/blob/main/01_web_html/03_html_link_img.html)
  * [div, span tag](https://github.com/KimJinYeon/LikeLion_13th_DataCourse/blob/main/01_web_html/04_html_div_span.html)
  * [summary](https://github.com/KimJinYeon/LikeLion_13th_DataCourse/blob/main/01_web_html/05_html_summary.html)
  * [자기소개 페이지](https://kimjinyeon.github.io/LikeLion_13th_DataCourse/01_web_html/kimjinyeon/main.html)
    
  #### CSS 기본 실습
  * [나의 갤러리 만들기](https://kimjinyeon.github.io/LikeLion_13th_DataCourse/02_css_practice/11_img_gallery.html)
  
  #### 웹 크롤링
  * [코스닥 정보 수집 코드](https://github.com/KimJinYeon/LikeLion_13th_DataCourse/blob/main/04_web_data/07_kosdaq.py)
    - [코스닥 정보 수집 csv 20210908](https://github.com/KimJinYeon/LikeLion_13th_DataCourse/blob/main/04_web_data/kosdaq_csv)
  * [영화 댓글 수집 코드(코다)](https://github.com/KimJinYeon/LikeLion_13th_DataCourse/blob/main/04_web_data/12_review2.py)
    - [영화 댓글 수집 csv(코다)](https://github.com/KimJinYeon/LikeLion_13th_DataCourse/blob/main/04_web_data/코다댓글.csv)
    - [코다 인포그래픽](https://kimjinyeon.github.io/LikeLion_13th_DataCourse/04_web_data/김진연_wordcloud_코다.png)
  * [jupyter 기반 영화 댓글 수집 코드(스파이더맨)](https://github.com/KimJinYeon/LikeLion_13th_DataCourse/blob/main/05_selenium/movie.ipynb)
    - [스파이더맨 리뷰 csv](https://github.com/KimJinYeon/LikeLion_13th_DataCourse/blob/main/05_selenium/%EC%8A%A4%ED%8C%8C%EC%9D%B4%EB%8D%94%EB%A7%A8%EB%A6%AC%EB%B7%B0.csv)
    - [jupyter 기반 스파이더맨 인포그래픽](https://github.com/KimJinYeon/LikeLion_13th_DataCourse/blob/main/05_selenium/wordcloud_%EC%8A%A4%ED%8C%8C%EC%9D%B4%EB%8D%94%EB%A7%A8.png)
    - .csv 파일을 엑셀로 열면 인코딩 문제가 생긴다: 엑셀은 ANSI/EUC-KR를 사용하기 때문
    - .csv 파일을 생성할 때, encoding='utf-8-sig' 파라미터를 이용하여 생성하면 문제 없이 읽을 수 있다.
    - sig는 signiture를 의미한다. 우리는 읽을 수 없지만, 컴퓨터는 BOM을 이용하여 인코딩 방식을 인식한다.
    - UTF-8은 BOM이 필요 없지만, 오류가 날 경우 일부러 표시해 줄 수 있다.
    - utf-8-sig는 파일의 맨 처음에 16진수 EF BB BF를 표기하는 것과 동일한 효과이다.(20210910 추가)

  #### 셀레니움
  * [jupyter 기반 셀레니움 활용 기초](https://github.com/KimJinYeon/LikeLion_13th_DataCourse/blob/main/05_selenium/selenium.ipynb)
  * [jupyter 기반 셀레니움 활용 - 아마존 상품 정보 찾기](https://github.com/KimJinYeon/LikeLion_13th_DataCourse/blob/main/05_selenium/selenium2.ipynb)
    - [아마존 상품 1개의 리뷰 크롤링](https://github.com/KimJinYeon/LikeLion_13th_DataCourse/blob/main/05_selenium/amazon_computer_review.csv)
  * [아마존 상품 리뷰 크롤링(실패)](https://github.com/KimJinYeon/LikeLion_13th_DataCourse/blob/main/05_selenium/amazon_review.py)
    - [아마존 정책](https://www.amazon.com/robots.txt)
    - 아마존은 고객 리뷰와 관련한 데이터를 대규모로 수집하는 것을 허용하지 않고 있다. (20210910 추가)
    - 여러 페이지를 탐색할 때, 크롬을 켜지 않고 하는 것이 편리하다는 것을 알게 되었다.
      + ChromeOptions에서 add_argument('headless')로 설정 가능

