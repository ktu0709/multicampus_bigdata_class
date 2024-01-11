import requests
from bs4 import BeautifulSoup
def crawl(url):
    data = requests.get(url)
    print(data)
    return data.content

def parse(pageString):
    bsObj = BeautifulSoup(pageString, "html.parser")
    noToday = bsObj.find("p", {"class":"no_today"})
    blind = noToday.find("span", {"class":"blind"})
    price = blind.text
    return price


url = "https://finance.naver.com/item/main.nhn?code=068270"
pageString = crawl(url) # 6671
price = parse(pageString)
print("price:", price)

