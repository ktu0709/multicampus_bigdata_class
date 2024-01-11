from bs4 import BeautifulSoup
import requests

r = requests.get('https://www.python.org/')
soup = BeautifulSoup(r.content, 'html.parser') #전체 문서를 객체로 리턴


res = soup.select('#content > div > section > div:nth-child(2) > div > p:nth-child(2)')
for i in res:
    print(i.get_text())

