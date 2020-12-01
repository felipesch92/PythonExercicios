#Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento. Para salários superiores
# a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
s = float(input('Informe seu salário: '))
if s > 1250:
    s = s * 1.1
else:
    s = s * 1.15
print('Parabéns, seu novo salário é de : R$ {:.2f}'.format(s))
#ctrl+q mostra a documentação