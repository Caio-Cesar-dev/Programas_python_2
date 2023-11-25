"""Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso,
 você deve mostrar, para cada palavra, quais são as suas vogais."""
palavras=('Banana','abacate','pera','cachorro','leao','macaco','urso', 'aprender','correr','laranjada')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

