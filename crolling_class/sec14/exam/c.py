from bs4 import BeautifulSoup , Comment
markup = "<b><!--Hey, buddy. Want to buy a used parser?-->abc</b>"
soup = BeautifulSoup(markup, 'html.parser')

coment = []
text_all = []

#for ele in soup.recursiveChildGenerator():
for ele in soup.b.children:
    if isinstance(ele,Comment):
        coment.append((ele))
    elif isinstance(ele,str):
        text_all.append(ele.strip())


print(coment)
print(text_all)