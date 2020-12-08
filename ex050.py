#Desenvolva um programa que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
n = []
s = 0
for x in range(0, 6):
    n.append(int(input('Digite o {} valor: '.format(x+1))))
print(n)
for x in range(0, 6):
    if n[x] % 2 == 0:
        s += n[x]
print('A soma dos valores pares é de : {}'.format(s))
