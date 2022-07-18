import requests
from bs4 import BeautifulSoup

url = 'https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту'

names_dict = {}
while True:
    req = requests.get(url)

    soup = BeautifulSoup(req.text, 'lxml')
    fragment = soup.find('div', id='mw-pages')

    for nam in fragment.find_all('div', class_='mw-category-group'):
        category = nam.h3.text
        animal_names = [[x.text, f"https://ru.wikipedia.org{x.a['href']}"] for x in nam.find_all('li')]

        if not names_dict.get(category):
            names_dict[category] = []
        names_dict[category] = names_dict[category] + animal_names

    hrf = fragment.find_all('a')[-1]
    url = f"https://ru.wikipedia.org{hrf['href']}"
    if hrf.text != 'Следующая страница':
        break

# выводим количество запмсей на букву
for x, y in names_dict.items():
    print(x, len(y))
