from bs4 import BeautifulSoup

html_doc = """
<html>
<body>
<table>
<tr>
  <th>Name</th>
  <th>Age</th>
</tr>
<tr>
  <td>John</td>
  <td>25</td>
</tr>
<tr>
  <td>Alice</td>
  <td>30</td>
</tr>
</table>
</body>
</html>
"""


soup = BeautifulSoup(html_doc, 'html.parser')  #전체 문서 객체로 리턴

# 테이블이 여러개  -> table의 id, css로  객체를 지정해서 하위로 탐색
table_data = []
rows = soup.find_all('tr')
for row in rows:
    cells = row.find_all('td')
    data = [cell.get_text() for cell in cells]
    table_data.append(data)


for data in table_data:
    print(data)
