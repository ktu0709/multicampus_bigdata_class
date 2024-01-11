from bs4 import BeautifulSoup

html_doc = """
<html>
<body>
<div class="container">
  <h1>Heading</h1>
  <div class="content">
    <p>Paragraph 1</p>
    <p>Paragraph 2</p>
  </div>
</div>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

heading = soup.find('h1').get_text()
paragraphs = [p.get_text() for p in soup.select('.content p')]

print("Heading:", heading)
print("Paragraphs:", paragraphs)

### 위의 html 코드를 css의사 결정 으로 선택해서  데이터 추출 해 보자.  paragraphs
heading = soup.select_one('h1').get_text()
first_paragraph = soup.select_one('.content p:nth-of-type(1)').get_text()
second_paragraph = soup.select_one('.content p:nth-of-type(2)').get_text()

print("Heading:", heading)
print(first_paragraph, second_paragraph)


para_child = soup.select('p:nth-child(1)')
print(para_child[0].get_text())
para_child2 = soup.select('p:last-child')
print(para_child2[0].get_text())
para_extra = soup.select('p:nth-of-type(2)')
print(para_extra[0].get_text())
para = soup.select('p:first-child')
print(para[0].get_text())
para_hover = soup.select('p:hover')
print(para[0].get_text())