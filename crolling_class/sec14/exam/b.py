from bs4 import BeautifulSoup

markup = "<b><!--Hey, buddy. Want to buy a used parser?-->abc</b>"
soup = BeautifulSoup(markup, 'html.parser')
comment = soup.b.string
print(comment)
print(type(comment))

comment = soup.b.text
print(comment)
print(type(comment))

comment = soup.getText()
print(comment)
print(type(comment))
# <class 'bs4.element.Comment'>

