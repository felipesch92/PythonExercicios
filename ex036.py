#Exercício Python 36: Escreva um programa para aprovar o empréstimo
# bancário para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então
# o empréstimo será negado.
v_casa = float(input('Digite o valor do imóvel: R$ '))
v_sal = float(input('Digite o valor do seu salário: R$ '))
q_anos = int(input('Em quantos anos deseja pagar? '))
p_men = v_casa / (q_anos * 12)
if v_sal * 0.3 >= p_men:
    print('Parabéns empréstimo aprovado!')
    print('Você irá pagar {} prestaçoes no valor de R$ {:.2f}!'.format(q_anos * 12, p_men))
else:
    print('A prestação de R$ {:.2f} excede os 30% do seu salário de R$ {:.2f}'.format(p_men, v_sal))
    print('Empréstimo reprovado.')
