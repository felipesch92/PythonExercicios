#Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal
#– 3x ou mais no cartão: 20% de juros
valor = float(input('Digite o valor a ser pago: R$ '))
print('Qual a forma de pagamento?')
op = int(input('1 - à vista dinheiro/cheque - 2 à vista no cartão - 3 2x no cartão - 4 3x ou mais no cartão '))
if op == 1:
    v_final = valor * 0.9
elif op == 2:
    v_final = valor * 0.95
elif op == 3:
    v_final = valor
elif op == 4:
    v_final = valor * 1.2
    p = int(input('Quantas parcelas? '))
    print('Suas parcelas: {} vezes de R$ {:.2f}'.format(p, v_final / p))
else:
    print('Opção inválida')
print('O valor final para o seu produto é de: R$ {:.2f}'.format(v_final))
