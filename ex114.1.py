import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não esta acessivel no momento!')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    print(site.read())
