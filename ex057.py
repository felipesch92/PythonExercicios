#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
s = input('Digite seu sexo: [M/F] ').strip().upper()[0]
while s not in 'MF':
    s = input('Dados inválidos, Digite seu sexo: [M/F] ').strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(s))
