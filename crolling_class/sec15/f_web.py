from bs4 import BeautifulSoup

xml_doc = """
<bookstore> 
  <book category="fiction">
    <title lang="en">Harry Potter</title>
    <author>J.K. Rowling</author>
  </book>
  <book category="non-fiction">
    <title lang="en">The Power of Habit</title>
    <author>Charles Duhigg</author>
  </book>
</bookstore>
"""
'''
/bookstore  :  루트 요소 선택  , 최상위 루트엘리먼트이다.  
/bookstore/book   :  루트 요소의 book  직계자식 요소를 출력
//book :'book'의 다음의 모든 요소를 선택 
/bookstore/book/title
//book/title  : title에 대한 모든 요소를 선택  
//book[@category="non-fiction"] :  모든 book의 속성이    category="non-fiction 를 리턴
//title [@lang="en"] 

    / : 선택 / : 루트 요소 선택
   // : 모든 요소 선택
   element : 문서의 모든 수준에서 선택합니다.
   element/하위 엘리먼트  : 주어진 이름을 가진 모든 요소를 선택합니다.
   @attribute : 주어진 이름을 가진 속성을 선택합니다.
   predicate : 조건에 따라 요소를 필터링합니다.
'''

# Parse the XML document using BeautifulSoup
soup = BeautifulSoup(xml_doc, 'xml')

# Find all 'book' elements and extract the information
books = soup.find_all('book')
for book in books:
    category = book['category']
    title = book.find('title').text
    author = book.find('author').text

    print(f"Category: {category}")
    print(f"Title: {title}")
    print(f"Author: {author}")
    print()
