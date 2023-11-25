"""Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar
quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta."""
from random import randint
from time import sleep
print('-'*30)
print('     JOGO DA MEGA SENA')
print('-'*30)
jogos=[]
temp=[]
qt=int(input('Quantos jogos você deseja sortear: '))
print(f'-=-=-=-=-=Sorteando {qt} Jogos=-=-=-=-=-=-')
print()
for i in range(0,qt):
    for c in range(0,6):
        num=(randint(1,60))
        if num not in temp: #Não permite repetir numeros na msma lista
            temp.append(num)
        c+=1
    i+=1
    temp.sort()
    jogos.append(temp[:]) #copia os dados de temp joga uma lista de 6 numeros em jogos
    temp.clear() #limpa os dados de temp para não duplicar as listas
cont=0
for lista in jogos:
    cont+=1
    print(f'Jogo {cont}: ',end='')
    for elementos in lista:
        print([elementos],end=' ')
    sleep(1)
    print()
print()
print('BOA SORTE APOSTADOR!!!')

