import requests
from bs4 import BeautifulSoup

query = input("검색어를 입력하세요: ")
url = f'https://search.naver.com/search.naver?where=news&query={query}'

response = requests.get(url)
print('상태 코드:', response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')
titles = soup.select('span.sds-comps-text-type-headline1')

print('찾은 제목:', len(titles), '개')
for title in titles:
    print('-', title.get_text())
