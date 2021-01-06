# Faça um mini-sistema que utilize o Interactive Help do Python.
# O usuário vai digitar o comando e o manual vai aparecer.
# Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará.
def ajuda(comando):
    return help(comando)

while True:
    c = input('Qual comando você quer ajuda? ')
    ajuda(c)
    if c == 'FIM':
        break
