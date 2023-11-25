"""Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa
cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos."""
pessoas=0
home=0
mulher=0
while True:
    print('-'*20)
    print("CADASTRE UMA PESSOA")
    print('-'*20)
    id=int(input("Idade: "))
    sex= ' '
    while sex not in "MF":
        sex=str(input("Sexo: [M/F]")).upper()
    print('-'*20)

    if id > 18:
        pessoas +=1
    if sex == 'M':
        home+=1
    if sex == 'F':
        if id < 20:
            mulher +=1
    s_n = ' '
    while s_n not in "SN":
        s_n = str(input("Quer continuar? [S/N] ")).upper()
    if s_n == 'N':
        print(f"Total de pessoas com mais de 18 anos: {pessoas} \nAo todo temos {home} homem cadastrados\nE temos {mulher} mulheres com menos de 20 anos")
        break

