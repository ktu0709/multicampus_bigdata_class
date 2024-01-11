from bs4 import BeautifulSoup
'''
nth-of-type() 부모 요소 내의 위치에 따라 요소를 선택할 수 있는 CSS 의사 클래스 선택기
name = row.select_one('td.my').get_text(strip=True)
age = row.select_one('td:nth-of-type(2)').get_text(strip=True)
city = row.select_one('td:nth-of-type(3)').get_text(strip=True)
'''

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
data = []
rows = soup.select('table tr')
for row in rows[1:]:
    name = row.select_one('td:nth-of-type(1)').get_text(strip=True)
    age = row.select_one( 'td:nth-of-type(2)').get_text(strip=True)
    data.append({'Name': name, 'Age': age})

for item in data:
    print(f"Name: {item['Name']}, Age: {item['Age']}")


