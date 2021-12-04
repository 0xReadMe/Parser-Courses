import requests
from bs4 import BeautifulSoup

currency = []
price = []
page = requests.get('https://cbr.ru/key-indicators/')
soup = BeautifulSoup(page.text, "lxml")

if page.status_code == 200:
    def parse_course():
        """ Parse course """
        currency_find = soup.find_all('div', {'class': 'd-flex title-subinfo'})
        price_find = soup.find_all('td', class_='value td-w-4 _bold _end mono-num')
        for curr in currency_find:
            currency_sort = curr.find('div', {'class': 'col-md-5'}).text.strip()
            currency.append(currency_sort)
        for i in price_find:
            price.append(i.get_text())
        print_course()


    def print_course():
        """ Print course """
        diction = dict(zip(currency, price))
        for key in diction:
            print('Курс', key, 'на сегодня:', diction[key])
else:
    print(f'Error: {page.status_code}')

parse_course()
