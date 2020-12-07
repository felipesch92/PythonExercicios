#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu
# Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#– IMC abaixo de 18,5: Abaixo do Peso
#– Entre 18,5 e 25: Peso Ideal
#– 25 até 30: Sobrepeso
#– 30 até 40: Obesidade
#– Acima de 40: Obesidade Mórbida
peso = float(input('Informe seu peso: (Kg) '))
altura = float(input('Informe sua altura: '))
imc = peso / (altura ** 2)
print('Seu IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    res = 'Abaixo do Peso'
elif imc >= 18.5 and imc <= 25:
    res = 'Peso Ideal'
elif imc > 25 and imc <= 30:
    res = 'Sobrepeso'
elif imc > 30 and imc <= 40:
    res = 'Obesidade'
else:
    res = 'Obesidade Mórbida'
print('Você está: {}'.format(res))
