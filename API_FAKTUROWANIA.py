import requests

lista_faktur = "https://jaco-z.fakturownia.pl/invoices.json?period=this_month&page=1&per_page=25&api_token=7Dlt0jbtcpSJKSqOco"

api_token = "7Dlt0jbtcpSJKSqOco"

headers = { "Authorization": f"Bearer {api_token}" }

def lista_faktur():
    response = requests.get(lista_faktur, headers=headers)
    #print(response.status_code)
    data = response.json()
    print(data)

def id_faktura():
    id = input("Podaj id:")
    response = requests.get("https://jaco-z.fakturownia.pl/invoices/191693535.json?api_token=7Dlt0jbtcpSJKSqOco?per_page={id}")
    data = response.json()
    print(data)

lista_faktur()
id_faktura()
