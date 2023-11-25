"""Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual
foi o maior e o menor valor digitado e as suas respectivas posições na lista."""
lista=[]
ultimo=5
x=0
maior=0
menor=0
for x in list(range(0,ultimo)):
    valor=int(input('Digite os valores para a lista: '))
    x+=1
    lista.append(valor)
    if valor > maior:
        maior = valor
    if x == 1:
        menor=valor
    else:
        if valor < menor:
            menor = valor
print(f'A lista completa: {lista}')
print(f'O maior valor é: {maior} e está localizado na posição, ',end='')
for i, v in enumerate(lista):
    if v ==maior:
        print(f'{i}...',end='')
print()
print(f'O valor menor é: {menor} e está localizado na posição, ',end='')
for i, v in enumerate(lista):
    if v ==menor:
        print(f'{i}...',end='')

