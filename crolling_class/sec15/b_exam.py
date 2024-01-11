from bs4 import BeautifulSoup
import requests

r = requests.get('https://www.python.org/')
if r.status_code == 200:
    print('connect')

print(r.text)
print(type(r.text))

soup = BeautifulSoup(r.content, 'html.parser') #전체 문서를 객체로 리턴
#print(soup.prettify())