from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep

# Edge 브라우저 옵션 설정
options = webdriver.EdgeOptions()
# Edge 드라이버 초기화
driver = webdriver.Edge(options=options)
driver.get("https://www.naver.com")

# 특정 요소(레시피 탭)를 찾아 클릭
sleep(5)  # 웹페이지 로드 대기
element = driver.find_element(By.CSS_SELECTOR, "#feed > div.ContentHeaderView-module__content_header___nSgPg > div > ul > li:nth-child(5) > a")
element.click()
sleep(5)  # 탭 내용 로드 대기

# 현재 페이지의 HTML 가져오기
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

# 레시피 항목을 찾음
recipe_items = soup.select('.HighlightedColumnView-module__common_highlighted_item___CNhUf')

# 각 항목에 대한 정보 추출 및 출력
for item in recipe_items:
    # 이미지 URL 추출
    img_url = item.select_one('.ImgView-module__content_img___QA0gl img')['src']
    # 제목 추출
    title = item.select_one('.HighlightedColumnView-module__title___YGJU_').text.strip()
    # 설명 추출
    description = item.select_one('.HighlightedColumnView-module__sub___AbKQL').text.strip()
    print(f"이미지 URL: {img_url}, 제목: {title}, 설명: {description}")

# 드라이버 종료
driver.quit()
