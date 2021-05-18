import requests

try:
    resposta = requests.get('http://pudim.com.br')
    status = resposta.status_code
except:
    print('\033[1;33mO site Pudim nõa está acessivel no momento!\033[m')
else:
    print('\033[1;32mO site Pudim está acessivel!\033[m')
