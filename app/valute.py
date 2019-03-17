import datetime
import xml.etree.ElementTree as ElementTree
import requests 

def find_element(root,code_valute):
    for Valute in root.iter('Valute'):
        if Valute.find('CharCode').text == code_valute:
            return Valute.find('Value').text
    return 'Такой валюты нет'
def rate_of_exchange(code_valute,date_rate):
    try:
        rate_url = "http://www.cbr.ru/scripts/XML_daily.asp"
        xml = requests.get(rate_url,params = f'date_req={date_rate}')
        xml.raise_for_status()
        root = ElementTree.fromstring(xml.content)
        result = find_element(root,code_valute)
        return result
    except (requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False
    return False
if __name__ == '__main__': 
    print(rate_of_exchange('EUR',datetime.datetime.today().strftime("%d/%m/%Y")))
   
