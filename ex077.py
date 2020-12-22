# Crie um programa que tenha uma tupla com várias palavras
# (não usar acentos). Depois disso, você deve mostrar, para
# cada palavra, quais são as suas vogais.
palavras = ('Livro', 'Caderno', 'Lapis', 'Caneta', 'Notebook', 'Chimarrao', 'Teclado')
v = ''
for p in palavras:
    print(f'\nNa palavra {p.upper()} se encontram as vogais ', end='')
    for l in p:
        if l in 'aeiou':
            print(l.upper(), end=' ')
