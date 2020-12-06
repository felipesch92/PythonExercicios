#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
num = int(input('Digite um número inteiro qualquer: '))
op = int(input('Digite a opção: 1 - Binário 2 - Octal 3 - Hexadecimal: '))
res = ''
while op < 1 or op > 3:
    print('Opção errada, digite novamente: ')
    op = int(input('1 - Binário 2 - Octal 3 - Hexadecimal: '))
if op == 1:
    while num >= 1:
        if num % 2 == 1:
            res = res+'1'
        else:
            res = res+'0'
        num = num // 2
    res = res[::-1]
elif op == 2:
    if num >= 8:
        while num >= 8:
            res = res + str(num % 8)
            num = num // 8
        if num < 8:
            res = res + str(num)
        res = res[::-1]
    else:
        res = num
elif op == 3:
    if num >= 16:
        while num >= 16:
            if num % 16 == 10:
                c_hex = 'A'
            elif num % 16 == 11:
                c_hex = 'B'
            elif num % 16 == 12:
                c_hex = 'C'
            elif num % 16 == 13:
                c_hex = 'D'
            elif num % 16 == 14:
                c_hex = 'E'
            elif num % 16 == 15:
                c_hex = 'F'
            else:
                c_hex = str(num % 16)
            res = res + c_hex
            num = num // 16
        if num < 16:
            res = res + str(num)
        res = res[::-1]
    else:
        res = num
print(res)
