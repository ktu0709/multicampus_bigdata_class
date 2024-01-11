from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep

# Edge 브라우저 옵션 설정
options = webdriver.EdgeOptions()

# Edge 드라이버 초기화
driver = webdriver.Edge(options=options)

# 중앙일보 오피니언 페이지 열기
driver.get("https://www.joongang.co.kr/opinion")
sleep(5)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text(separator='\n').strip()
cleaned_text = "\n".join([line for line in text.split('\n') if line.strip() != ''])
# 출력
print(cleaned_text)
# 드라이버 종료
driver.quit()

