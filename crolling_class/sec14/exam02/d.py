from bs4 import BeautifulSoup

with open("D:\multicampus\python_pjt\sec14\exam02\sec03\olview02.html",encoding='UTF8') as file:
    soup = BeautifulSoup(file, 'html.parser')


#print(ol2_soup.prettify())

id_res = soup.select_one('#q1')
if id_res:
    print(id_res.get_text())


class_res = soup.select('.a1')
for tag in class_res:
    print(tag.get_text())


id_res = soup.find(id='q1')
if id_res:
    print(id_res.get_text())


class_res = soup.find_all(class_='a1')
for tag in class_res:
    print(tag.get_text())