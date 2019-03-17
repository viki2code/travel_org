import datetime
import xml.etree.ElementTree as ElementTree
import requests 

def find_element(root,code_valute):
    for Valute in root.iter('Valute'):
        if Valute.find('CharCode').text.upper() == code_valute.upper():
            currency_data = {'name_of_currency': Valute.find('Name').text,
                            'rate': Valute.find('Value').text}
            return currency_data
    currency_data = {'name_of_currency': 'Указанная валюта не найдена',
                            'rate': ''}
    return currency_data
def get_currency(date_rate):
    rate_url = "http://www.cbr.ru/scripts/XML_daily.asp"
    xml = requests.get(rate_url,params = f'date_req={date_rate}')
    xml.raise_for_status()
    root = ElementTree.fromstring(xml.content)
    return root

def all_currency(date_rate):
    i = 0
    currencies_name = []
    root = get_currency(date_rate)
    for Valute in root.iter('Valute'):
        i += 1
        new = (1,Valute.find('CharCode').text.upper())
        currencies_name.append(new)
        
    return currencies_name
def rate_of_exchange(code_valute,date_rate):
    try:
        root = get_currency(date_rate)
        result = find_element(root,code_valute)
        return result
    except (requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False
    return False
if __name__ == '__main__': 
    r = all_currency()
    print(r[0])  
    #print(rate_of_exchange('EUR',datetime.datetime.today().strftime("%d/%m/%Y")))
   
