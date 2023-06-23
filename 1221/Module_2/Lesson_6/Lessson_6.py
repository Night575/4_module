import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.cbr.ru/scripts/XML_daily.asp")
soup = BeautifulSoup(response.content, features="xml")
print(soup)


def get_course(course_id):
    australian_dollar = soup.find("Valute", ID=course_id)

    currency_nominal = australian_dollar.Nominal.text
    currency_value = australian_dollar.Value.text
    currency_name = australian_dollar.Name.text

    print(f'({currency_nominal} шт.) {currency_name} стоит(ят) {currency_value} руб.')
    

currencies_list = soup.find_all("Valute")
for currency in currencies_list:
    get_course(currency["ID"])