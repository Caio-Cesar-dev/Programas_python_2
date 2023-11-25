"""Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista
composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de
cada aluno individualmente."""
lista_prin=[]
while True:
    nome=str(input('Digite o nome do aluno: ')).upper()
    nota1=float(input('Digite a primeira nota: '))
    nota2=float(input('Digite a segunda nota: '))
    media=(nota1+nota2)/2
    lista_prin.append([nome,nota1,nota2,media])
    s_n=str(input("Deseja continuar (S/N): ")).upper()
    if s_n in 'SN':
        break
print('-=-'*10)
print('Nº. NOME      MÉDIA')
print('-'*30)
for i, a in enumerate(lista_prin):
    print(f'{i:<4}{a[0]:<10}{a[3]:>8.1f}  ')
print('-'*30)
while True:
    aluno_nota=int(input("Mostrar nota de qual aluno (999 interrompe)? "))
    if aluno_nota == 999:
        break
    if aluno_nota in range(0,len(lista_prin)):
        print(f'Notas de {lista_prin[aluno_nota][0]} são: {lista_prin[aluno_nota][1:3]}')
print('FINALIZANDO...')
print("<<< VOLTE SEMPRE!! >>>")
