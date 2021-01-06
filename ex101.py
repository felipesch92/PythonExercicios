# Crie um programa que tenha uma função chamada voto() que vai receber como
# parâmetro o ano de nascimento de uma pessoa, retornando um valor
# literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def voto(ano_nasc):
    from datetime import date
    idade = date.today().year - ano_nasc
    v = ''
    if 18 <= idade <= 69:
        v = 'OBRIGATÓRIO'
    elif idade < 16:
        v = 'NEGADO'
    else:
        v = 'OPCIONAL'
    return v, idade


while True:
    ano_nasc = int(input('Ano Nascimento: '))
    if ano_nasc == 999:
        break
    v, idade = voto(ano_nasc)
    print(f'O seu voto é {v} por que sua idade é de {idade}')
