import requests
from bs4 import BeautifulSoup
from datetime import datetime

today = datetime.today().strftime("%d.%m.%Y")

response = requests.get('https://www.cbr.ru/scripts/XML_daily.asp', params={'date_req': today})

def get_course(currency_id):
    soup = BeautifulSoup(response.content, features='xml')

    valute = soup.find('Valute', ID=currency_id)

    valute_value = valute.Value.text

    valute_name = valute.Name.text

    valute_info = {'name': valute_name, 'value': valute_value}

    return valute_info



