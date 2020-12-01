from datetime import date
print('Coloque 0 para analisar o ano atual')
ano = int(input('Digite um ano para saber se é bissexto: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            b = True
        else:
            b = False
    else:
        b = True
else:
    b = False
if b == True:
    print('O ano de {} é bissexto!'.format(ano))
else:
    print('O ano de {} não é bissexto!'.format(ano))
