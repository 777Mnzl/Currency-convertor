from requests import get
from pprint import PrettyPrinter

BASE_URL = 'https://free.currconv.com/'
API_KEY = #'use your own api here from currency convertor website' 


printer = PrettyPrinter()


def get_currencies():
    endpoint = f'api/v7/currencies?apiKey={API_KEY}'
    url = BASE_URL + endpoint
    data = get(url).json()['results']

    data = list(data.items())
    data.sort()



    return data

def print_currencies(currencies):
    for name, currency in currencies:
        name = currency['currencyName']
        _id = currency['id']
        symbol = currency.get('currencySymbol', '')
        print(f'{_id} - {name} - {symbol}')



def exchange_rate(curr1, curr2):
    endpoint = f'api/v7/convert?q={curr1}_{curr2}&compact=ultra&apiKey={API_KEY}'
    url = BASE_URL + endpoint
    data = get(url).json()

    if len(data) == 0:
        print('Invalid Currency')
        return
    
    rate = list(data.values())[0]
    print(f'{curr1} --> {curr2} = {rate}')

    return list(data.values())[0]

def convert(curr1,curr2, amount):
    rate = exchange_rate(curr1, curr2)
    if rate is None:
        return
    try:
        amount = float(amount)
    except:
        print('invalid amount.')
        return

    converted_amount = rate * amount
    print(f'{amount} {curr1} is equal to {converted_amount} {curr2}')


def main():
    currencies = get_currencies()
    print('Welcome to the currency convertor by Manzil')
    print('List - lists the different currencies')
    print('Convert - convert one currency to another')
    print('Rate - get exchange rate of two currencies')
    print()

    while True:
        command = input('Enter a command(q to quit): ').lower()
        if command == 'q':
            break

        elif command == 'list':
            print_currencies(currencies)
        elif command == 'convert':
            currency1 = input('Enter a currency name: ').upper()
            amount = input(f'enter an amount in {currency1}:')
            currency2 = input('Enter a currency name to convert: ').upper()
            convert(currency1, currency2,amount)
        elif command == 'rate':
            currency1 = input('Enter a currency name : ').upper()
            currency2 = input('Enter another currency name: ').upper()
            exchange_rate(currency1,currency2)
        else:
            print('unrecognized command')

main()
