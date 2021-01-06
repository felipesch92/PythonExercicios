# Faça um programa que tenha uma função notas() que pode receber
# várias notas de alunos e vai retornar um dicionário com as seguintes
def f_notas(*notas, sit=True):
    """
    -> Função que mostra o boletim de um aluno
    :param notas: As notas do aluno
    :param sit: Se é para mostrar ou não a situação do aluno
    :return: retorna o boletim do aluno
    """
    boletim = {}
    boletim['total'] = len(notas)
    boletim['maior'] = max(notas)
    boletim['menor'] = min(notas)
    media = sum(notas) / len(notas)
    boletim['media'] = f'{media:.2f}'
    if sit:
        if media < 7:
            boletim['situacao'] = 'RUIM!'
        else:
            boletim['situação'] = 'BOA!'
    return boletim


resp = f_notas(9.7, 4, 10, 8, 7)
resp1 = f_notas(8, 5, 8, 9.5, 4.5, sit=False)
print(resp)
print(resp1)
