# файл для парсинга данных с сайта

import requests
from bs4 import BeautifulSoup
from data_and_file_writer import min_price, max_price, file_writer

link = 'https://www.ligakvartir.ru/lugansk/snyat-nedvizhimost'

def site_parse(link):
    headings = ['цена', 'ссылка', 'адрес']
    file_writer(headings)

    st_accept = "text/html"
    st_useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"

    r = requests.get(link, headers= {'User-Agent': 'Custom'}, timeout= (5, 10))

    bs = BeautifulSoup(r.text, 'lxml')
    elements = bs.find_all('div', class_='col-x col-lg-4 col-sm-6 col-xs-6')
    for element in elements:

        price_and_currency = element.find('div', class_="price sale").span.string
        price = ''
        for i in price_and_currency:
            if i.isdigit():
                price += i
        price = int(price)

        if price > max_price or price < min_price:
            continue

        link = element.find('div', class_='object_title').a['href']
        adress = ''
        parts_of_adress = element.find('div', class_='object_desc city-rayon')
        for s in parts_of_adress.find_all('a', string= True):
            adress+=s.string + ' '
        

        offer = [price, link, adress]

        file_writer(offer)