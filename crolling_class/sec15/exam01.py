# 1. 웹에서 html 문서를 가져와 beautifulsoup 으로 파싱
from bs4 import BeautifulSoup
import urllib.request  # 웹상의 url 을 파이썬이 인식할 수 있도록 해주는 모듈
def exam01():
    list_url = "http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?hmpMnuId=106"
    url = urllib.request.Request(list_url)

    result = urllib.request.urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup( result, "html.parser")
    # 2. 시청자 게시판의 날짜와 본문 내용을 가져옵니다.
    result1 = soup.find_all('span', class_='date')
    result2 = soup.find_all('p', class_='con')

    # 3. 시청자 게시판의 날짜와 본문을 params 와 params2 리스트에 담습니다.
    params1 = []
    params2 = []
    for i in result1:
        params1.append(i.get_text("  ", strip=True))
    for i in result2:
        params2.append(i.get_text("  ", strip=True))

    # 4. 날짜와 본문을 같이 출력 합니다.
    for k, h in zip(params1, params2):
        print(k + '   ' + h)

def exam_all():
    # 1. 웹에서 html 문서를 가져와 beautifulsoup 으로 파싱
    from bs4 import BeautifulSoup
    import urllib.request  # 웹상의 url 을 파이썬이 인식할 수 있도록 해주는 모듈

    for i in range(1, 23):
        list_url = ('http://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page=' +str(i) + '&hmpMnuId=106&searchKeywordValue=0&bbsId=10059819&searchKeyword=&searchCondition=&searchConditionValue=0&')
        url = urllib.request.Request(list_url)
        result = urllib.request.urlopen(url).read().decode("utf-8")
        soup = BeautifulSoup(result, "html.parser")

        # 2. 시청자 게시판의 날짜와 본문 내용을 가져옵니다.
        result1 = soup.find_all('span', class_='date')
        result2 = soup.find_all('p', class_='con')

        # 3. 시청자 게시판의 날짜와 본문을 params 와 params2 리스트에 담습니다.
        params1 = []
        params2 = []
        for i in result1:
            params1.append(i.get_text("  ", strip=True))
        for i in result2:
            params2.append(i.get_text("  ", strip=True))

        # 4. 날짜와 본문을 같이 출력 합니다.
        for k, h in zip(params1, params2):
            print(k + '   ' + h)
if __name__ == '__main__':
    exam_all()