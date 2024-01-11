from bs4 import BeautifulSoup
import requests
# naver -> 웹툰 -> 웹소설
resp = requests.get('https://novel.naver.com/webnovel/weekday')
soup = BeautifulSoup(resp.text, 'html.parser')
# print(soup)

lanking_list = soup.find('div', class_='component_section')
#print(lanking_list)

# //*[@id="integrationRaking"]
#integrationRaking
#integrationRaking > ul:nth-child(1) > li:nth-child(1)
item_list = lanking_list.find_all('li', class_='item')
#print(item_list)

for item in item_list:
    lank = item.p.text.strip()
    # title = item.find_all('p')[1].find('span', class_='title').text
    title = item.select('span.title')[0].text
    #print(f'{lank}위 : {title}')

# 연령별 인기작을 출력해보자
age_div = soup.select('#content > div:nth-child(5) > div.component_left_area')
#print(age_div)


for item in age_div:
        img_alt = item.select('img')
        for i in img_alt:
            alt_val = i.get('alt','')
            print(alt_val)