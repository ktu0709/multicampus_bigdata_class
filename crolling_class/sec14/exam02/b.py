from bs4 import BeautifulSoup

with open("D:\multicampus\python_pjt\sec14\exam02\sec03\olview02.html",encoding='UTF8') as file:
    ol2_soup = BeautifulSoup(file, 'html.parser')


#print(ol2_soup.prettify())

css_classes = set()
class_id = set()

for tag in ol2_soup.find_all(True):
    if 'class' in tag.attrs:
        css_classes.update(tag['class'])

    if 'id' in tag.attrs:
        class_id.add(tag['id'])


print("css_classes: ",css_classes)
print("class_id: ",class_id)
