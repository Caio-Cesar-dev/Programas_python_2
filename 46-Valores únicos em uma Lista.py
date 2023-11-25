"""Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma
lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos
digitados, em ordem crescente."""
lista=[]

while True:
    cadastro=int(input("digite um numero: "))

    if cadastro in lista:
        print('Valor duplicado! Não Será adicionado!')
    if cadastro not in lista:
        lista.append(cadastro)
        s_n=str(input('Deseja continuar [S/N]: ')).upper()
    if s_n not in 'SN':
        print('Digite S para continuar ou N para sair!!')
    if s_n == 'N':
        break
    else:
        if s_n=='S':
            continue
lista.sort()
print(f'Os elementos da lista são:{lista}  ')

