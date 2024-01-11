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
  <td class = 'my'  >John</td>
  <td>25</td>
  <td  class = 'my' >New York</td>
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

my_texts = [td.get_text(strip=True) for td in soup.select('td.my')]

print("Texts:", my_texts)

output_text = ', '.join(my_texts)
print("Output Text:", output_text)

