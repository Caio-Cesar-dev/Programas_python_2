"""Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas
extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o
conteúdo das três listas geradas."""
lista=[]
impares=[]
pares=[]
while True:
    num=int(input("Digite um número: "))
    s_n=str(input('Deseja continuar [S/N]: ')).upper()
    lista.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    if s_n == 'N':
       break
    else:
       if s_n not in "SN":
           print("Digite apenas S(sim) ou N(não)!!")

print('-='*30)
print(f'A lista completa digitada foi: {lista}')
print(f'Os valores Impares foram: {impares}')
print(f'Os valores Pares foram: {pares}')