from bs4 import BeautifulSoup
# 요소의 속성 값 찾는 방법
html_doc = """
<html>
<body>
<h1>Links</h1>
<ul>
    <li><a href="https://www.example.com">Example 1</a></li>
     <li> <a href="https://www.google.com">Example 2</a></li>
     <li> <a href="https://www.openai.com">Example 3</a></li>
</ul>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
links = [a['href'] for a in soup.select('body ul li a')]

for link in links:
    print(link)

print('-----------------')

links = [a['href'] for a in soup.find_all('a')]

for link in links:
    print(link)