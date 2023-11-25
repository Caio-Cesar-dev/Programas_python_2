"""Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
quer ou não continuar a digitar valores."""
stop=''
cont=0
m=0
maior=0
menor=0
while stop != 'N':
    num=int(input("Digite um numero: "))
    stop=str(input("DESEJA CONTINUAR? [S/N]: ")).upper()
    cont +=1
    m= m + num
    if cont == 1: # o contado na primeira contagem cai aqui e atribui valores iguais para essas duas variaveis
        maior=num
        menor=num
    else:        #já no segundo loop entra aqui e começa a comparar com os valores recebidos antes
        if num > maior:
            maior=num
        if num < menor:
            menor=num
media= m/cont
print(f"Você digitou {cont} numeros e a média foi {media:.2f} ")
print(f"O maior numero {maior} e o menor foi {menor}")