#Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes
l1 = float(input('Primeira linha: '))
l2 = float(input('Segunda linha: '))
l3 = float(input('Terceira linha: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    if l1 == l2 and l1 == l3:
        tipo = 'EQUILÁTERO'
    elif l1 == l2 or l1 == l3 or l2 == l3:
        tipo = 'ISÓSCELES'
    else:
        tipo = 'ESCALENO'
    print('É possível formar um triângulo do tipo: {}'.format(tipo))
else:
    print('Não é possível formar um triângulo!')