#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi
# multado. A multa vai custar R$7,00 por cada Km acima do limite.
v = int(input('Informe a velocidade do carro: '))
if v > 80:
    m = (v - 80) * 7
    print('Você foi multado em R$ {:.2f} reais.'.format(m))
else:
    print('Parabéns você está andando no limite da velocidade permitida')
