import requests


def currency_rates(currency):
    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    if r.status_code == 200:
        for info_text in r.text.split('<CharCode>'):
            if currency == info_text.split('</CharCode>')[0]:
                info_text_2 = info_text.split('<Value>')[1]
                return float('.'.join(info_text_2.split('</Value>')[0].split(',')))


print(type(currency_rates('USD')))
print(currency_rates('USD'))
print(currency_rates('EUR'))
print(currency_rates('eur'))
