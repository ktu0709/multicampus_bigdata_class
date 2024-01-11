from bs4 import BeautifulSoup

with open('my_html.html') as file:
        soup = BeautifulSoup(file,'html.parser')

for i in soup.strings:
    print(repr(i))
