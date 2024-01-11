from bs4 import BeautifulSoup

html_doc = """
<html>
<body>
<table>
<tr>
  <th>Name</th>
  <th>Age</th>
  <th>City</th>
</tr>
<tr>
  <td>John</td>
  <td>25</td>
  <td>New York</td>
</tr>
<tr>
  <td>Alice</td>
  <td>30</td>
  <td>London</td>
</tr>
</table>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')  #전체 문서 객체로 리턴
#header 출력
#row 데이터 출력
headers = [th.get_text() for th in soup.select('table th')]

for th in soup.select('table th'):
    rows = [ [td.get_text() for td in row.select('td')]   for row in soup.select('table tr')[1:]  ]


print("Headers:", headers)
print("Rows:", rows)
