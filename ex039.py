#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do
# alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano
if idade < 18:
    print('Ainda faltam {} ano(s) para você se alistar!'.format(18 - idade))
elif idade > 18:
    print('Você passou {} ano(s) do prazo para se alistar!'.format(idade - 18))
else:
    print('Seu alistamento é neste ano letivo de {}!'.format(ano_atual))
