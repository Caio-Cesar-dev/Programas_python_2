"""Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""
lista=[]
while True:
    num=int(input('Digite numeros (0 para sair!!): '))
    if num == 0:
        break
    lista.append(num)

lista.sort(reverse=True)
print('-='*30)
print(f'O total de numeros digitados foram: {len(lista)}')
print(f'A lista ordenada decrescente {lista}')
if 5 in lista:
    print('O valor 5 está contido na lista!!')
else:
    print('O número 5 não está contido na lista')