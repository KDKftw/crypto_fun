from pycoingecko import CoinGeckoAPI
import re

cg = CoinGeckoAPI()


BTCprice = cg.get_price(ids='ethereum', vs_currencies='usd')
#BTCprice = cg.get_price(vs_currencies='usd')


print(BTCprice)
print(type(BTCprice))



print(BTCprice.values())
BTCpriceString = (str(BTCprice.values()))
temp = re.findall(r'\d+', BTCpriceString)
res = list(map(int, temp))
print(res)

print("|||||||||||||||||||||||||||||")


def returnCryptoPrice(crypto):
    price = cg.get_price(ids=crypto, vs_currencies='usd')
    priceString = (str(price.values()))
    temp = re.findall(r'\d+', priceString)
    #cryptoPrice = list(map(int, temp))
    #cryptoPrice = float(str, temp)
    cryptoPrice = tuple( temp)
    print(cryptoPrice)

    if len(cryptoPrice)>1:
        cryptoPriceStr = str(cryptoPrice[0]+"."+cryptoPrice[1])

        cryptoPriceFloat = float(cryptoPriceStr)
        print(cryptoPriceFloat)
        print(type(cryptoPriceFloat ))

    else:
        cryptoPriceFloat = float(cryptoPrice[0])
        print(cryptoPriceFloat)

    return(cryptoPriceFloat)

returnCryptoPrice("polkadot")
returnCryptoPrice("bitcoin")
returnCryptoPrice("dogecoin")