import requests

api_token = "7Dlt0jbtcpSJKSqOco"

headers = { "Authorization": f"Bearer {api_token}" }

def lista_faktur():
    lista = f"https://jaco-z.fakturownia.pl/invoices.json?period=this_month&page=1&per_page=25&api_token={api_token}"

    response = requests.get(lista, headers=headers)
    data = response.json()
    print(data)

def id_faktura():
    id = input("Podaj id:")

    faktura = f"https://jaco-z.fakturownia.pl/invoices/{id}.json?api_token={api_token}"

    response = requests.get(faktura, headers=headers)
    data = response.json()
    print(data)

while True:
    command = input()

    if command == 'list':
        lista_faktur()
        pass
    elif command == 'byid':
        id_faktura()
        pass
    else:
        print('No such command.')
        pass

    pass