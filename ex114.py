from urllib import request

url = input('Informe a url a ser testada: ')
try:
    site = request.urlopen(url)
    print(site)
except Exception as erro:
    print(erro)
else:
    print('Consegui aessar o site com sucesso!')
    print(site.read())
