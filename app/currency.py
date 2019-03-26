import xml.etree.ElementTree as ElementTree
import requests
from datetime import datetime


def find_element(root, code_valute):
    for valute in root.iter('Valute'):
        if valute.find('CharCode').text.upper() == code_valute.upper():
            currency_data = {'name_of_currency': valute.find('Name').text,
                             'rate': valute.find('Value').text}
            return currency_data
    currency_data = {'name_of_currency': 'Указанная валюта не найдена',
                     'rate': ''}
    return currency_data


def get_currency(date_rate=datetime.now().strftime("%d/%m/%Y")):
    rate_url = "http://www.cbr.ru/scripts/XML_daily.asp"
    xml = requests.get(rate_url, params=f'date_req={date_rate}')
    xml.raise_for_status()
    root = ElementTree.fromstring(xml.content)
    return root


def all_currency(date_rate=datetime.now().strftime("%d/%m/%Y")):

    currencies_name = []
    root = get_currency(date_rate)
    # for idx, valute in enumerate(root.iter('Valute')):
    for valute in root.iter('Valute'):

        new = (1, valute.find('CharCode').text.upper())
        print(valute.find('CharCode').text.upper())
        currencies_name.append(new)

    return currencies_name


def rate_of_exchange(
        code_valute,
        date_rate=datetime.now().strftime("%d/%m/%Y")):
    try:
        root = get_currency(date_rate)
        result = find_element(root, code_valute)
        return result
    except (requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False
    return False
