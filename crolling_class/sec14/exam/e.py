from bs4 import BeautifulSoup
css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'html.parser')
css_soup.find_all("p", class_="strikeout")
# [<p class="body strikeout"></p>]

css_soup.find_all("p", class_="body")
# [<p class="body strikeout"></p>]



rel_soup = BeautifulSoup('<p>Back to the <a rel="index first">homepage</a></p>', 'html.parser')


rel_soup.a['rel']
# ['index', 'first']
rel_soup.a['rel'] = ['index', 'contents']
print(rel_soup.p)
# <p>Back to the <a rel="index contents">homepage
# </a></p>

print("1.위 문서에 <a href=https://www.example.com>Example 1</a>를 추가해보자")
new_tag = rel_soup.new_tag('a',href="https://www.example.com")
new_tag.string = "Example 1"
rel_soup.append(new_tag)
print(rel_soup)


print("2.위 문서에 a가 가진 문자들만 추출해보자")
texts = [a.get_text() for a in rel_soup.find_all('a')]
print(texts)


print("2.위 문서에 a가 가진 주소 추출해보자")
hrefs = [a['href'] for a in rel_soup.find_all('a') if a.has_attr('href')]
print(hrefs)
