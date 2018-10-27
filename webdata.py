import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.douban.com/group/shafake/')
markup = r.text
print(r.text)
soup = BeautifulSoup(markup)
pattern = soup.find_all('br')
for item in pattern:
    print(item.string)
print(r.status_code)

