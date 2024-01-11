from bs4 import BeautifulSoup
import requests
# naver -> 웹툰 -> 웹소설
resp = requests.get('https://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106')
soup = BeautifulSoup(resp.text, 'html.parser')

post_list = soup.select('div.bhp.cmt_review  div.postList  ul.list.noThumb.spot_ li')



for item in post_list:
            userid = item.find('span',class_="userid").text.strip()
            comment =item.find('p',class_="con").text
            post_date = item.find('span',class_="date").text

            print(f"닉네임:{userid}\n 내용:{comment}\n 날짜:{post_date}\n")

