from bs4 import BeautifulSoup

with open("D:\multicampus\python_pjt\sec14\exam02\sec03\olview.html",encoding='UTF8') as file:
    ol_soup = BeautifulSoup(file, 'html.parser')

#print(ol_soup.prettify())
ol_tag = ol_soup.find_all('ol')


#for ol in ol_tag:
#    print(ol.prettify())

#
res = ol_soup.find_all('ol',{'type':'a'})
for ol in res:
    print(ol)
#

res02 = ol_soup.find_all('ol', {'type': 'A'})
li_test = [li.get_text() for ol in res02 for li in ol.find_all('li')]
for txt in li_test:
    print(txt)
