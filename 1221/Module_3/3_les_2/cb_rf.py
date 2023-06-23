import requests
from bs4 import BeautifulSoup


def get_dollar_course():
    return soup.find("Valute", ID="R01235").Value.text


responce = requests.get("https://www.cbr.ru/scripts/XML_daily.asp")
if responce.status_code == 200:
    soup = BeautifulSoup(responce.content, features="xml")