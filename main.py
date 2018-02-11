from bs4 import BeautifulSoup
import requests

r = requests.get('https://www.gamestop.com/trade/quote/nintendo-3ds/games/monster-hunter-generations/129531')
soup = BeautifulSoup(r.content, 'html.parser')
#myDivs = soup.findAll("div", {"class": "bigPrice ats-trade-quote-tradevalue-price"})
#final = myDivs.find("span", {"class": "priceAmount"})

for price in soup.find_all('div', attrs={'class': 'bigPrice ats-trade-quote-tradevalue-price'}):
    final = price.find('span', attrs={'class': 'priceAmount'})
    print(final.text)

#print(final.text)
print(soup.title)
