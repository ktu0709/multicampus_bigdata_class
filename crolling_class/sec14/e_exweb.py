from bs4 import BeautifulSoup

html_doc = """
<html>
<body>
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
  <li class="special">Item 3</li>
  <li>Item 4</li>
  <li class="special">Item 5</li>
</ul>
</body>
</html>
"""
soup = BeautifulSoup(html_doc, 'html.parser')  #전체 문서 객체로 리턴

print('1) :nth-child(n) - 부모의 n번째 자식 요소를 선택합니다.')
nth_child = soup.select('li:nth-child(3)')
print("nth-child:", nth_child,nth_child[0].get_text() )

print('2) td:nth-of-type ')
nth_of_type = soup.select('li:nth-of-type(2)')
print("nth-of-type:", nth_of_type ,nth_of_type[0].get_text() )

print('3) :last-child  ')
last_child = soup.select('li:last-child')
print("last-child:", last_child , last_child[0].get_text())

print('4. :not(selector)' )
not_selector = soup.select('li:not(.special)')
print("not selector:", not_selector)
for   res  in  not_selector:
    print(res.get_text())
