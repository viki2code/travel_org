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


def get_currency(date_rate=datetime.now()):
    rate_url = "http://www.cbr.ru/scripts/XML_daily.asp"
    date_rate_str = date_rate.strftime("%d/%m/%Y")
    xml = requests.get(rate_url, params=f'date_req={date_rate_str}')
    xml.raise_for_status()
    root = ElementTree.fromstring(xml.content)
    return root


def all_currency(date_rate=datetime.now()):
    currencies_name = []
    root = get_currency(date_rate)
    for idx, valute in enumerate(root.iter('Valute')):
    
        valute_tuple = (idx, valute.find('CharCode').text.upper())
        currencies_name.append(valute_tuple)

    return currencies_name


def rate_of_exchange(
        code_valute,
        date_rate=datetime.now()):
    
    try:
        root = get_currency(date_rate)
        result = find_element(root, code_valute)
        return result
    except (requests.RequestException, ValueError):
        
        return None
    
