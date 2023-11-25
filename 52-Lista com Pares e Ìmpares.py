"""Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente."""
listao=[[],[]]
valores=0
for x in range(1,8):
    valores=int(input(f'Digite o {x}º valor: '))
    if valores % 2==0:
        listao[0].append(valores)
    else:
        listao[1].append(valores)
listao[0].sort()
listao[1].sort()
print(f'Os valores ímpares são: {listao[1]}\nE os valores Pares são: {listao[0]}')