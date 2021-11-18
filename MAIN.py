import requests
from bs4 import BeautifulSoup
from VARIABLES import *

def getPrice(url):
    content = requests.get(url).text
    soup = BeautifulSoup(content, "html.parser")
    price = soup.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").text
    print(price)
    return price


def getPrice2():
    for url in URL_list:
        getPrice(url)

getPrice2()



