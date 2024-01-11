from bs4 import BeautifulSoup

with open('my_html.html') as file:
        soup = BeautifulSoup(file,'html.parser')

print(soup, type(soup))
print('-----------------')
print(soup.html.body.a)
print('-----------------')
print(soup.html.body.a['class'])
print('-----------------')
print(soup.html.body.a['id'])

print(help(soup.find()))
print('-----------------')
print(soup.find('p').text)

res = soup.findAll('a')
for i in res:
    print(i['href'])

print('-----------------')

res = soup.findAll('a')
for i in res:
    print(f"{i.text},{i['href']}")
