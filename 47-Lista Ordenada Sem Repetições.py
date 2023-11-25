"""Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma
lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela."""
lista=[]
for i in range(0,5):
    n=int(input("Digite um valor para a lista: "))
    if i ==0 or n > lista[-1]:#esse comando pega o ultimo elemento da lista
        lista.append(n)
        print(f'Adicionado ao final da lista...')
    else:
        pos=0
        while pos < len(lista): # vai percorrer as posições na lista e compara se o numero é menor
            if n <= lista[pos]:
                lista.insert(pos,n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos+=1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')


