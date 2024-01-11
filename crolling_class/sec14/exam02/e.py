from bs4 import BeautifulSoup
html_doc = """
<html>
<body>
<table>
<caption> list </caption>
<thead>
<tr>
  <th>Name</th>
  <th>Age</th>
  <th>City</th>
</tr>
</thead>
<tbody>
<tr>
  <td>John</td>
  <td>25</td>
  <td>New York</td>
</tr>
</tbody>
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

#1. 테이블의 제목인 thead의 문자열만 출력하자
thead = soup.select('table thead tr')
for i in thead:
    print(i.get_text().strip())


#2 tbody의 문자열만 출력하자
tbody = soup.select('table tbody tr')
for i in tbody:
    print(i.get_text().strip())

#3 1,2번으로 추출한 내용을 가지고 caption의 문자열을 파일명으로 지정해서 mylist.txt로 저장하자
fp_title= soup.select_one('body caption').get_text().strip()

with open(fp_title+'.txt','w') as fp:
    thead = soup.select('table thead tr')
    for i in thead:
        fp.write(i.get_text().strip())
    fp.write('\n')
    tbody = soup.select('table tbody tr')
    for i in tbody:
        fp.write(i.get_text().strip())
