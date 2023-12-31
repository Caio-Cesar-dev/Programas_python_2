"""Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
- Situação (opcional)"""

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: Uma ou mais notas dos alunos(aceita várias).
    :param sit: Valor opcional, indicando se deve ou não adcionar a situação.
    :return: Dicionário com várias informações sobre a situação da turma.
    """
    r= dict()
    r['total']= len(n)
    r['maior']= max(n)
    r['menor']= min(n)
    r['media']= sum(n) / len(n)
    if sit:
        if r['media']>=7:
            r['situação'] = 'BOA'
        elif r['media']>=5:
            r['situação']= 'RAZOÁVEL'
        else:
            r['situação']= 'RUIM'
    return r


#Programa principal
resp = notas(5.5, 4.6, 6.7, 9, sit=True)
print(resp)
#help(notas)