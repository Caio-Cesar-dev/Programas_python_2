"""Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha."""
matriz=[[0,0,0],[0,0,0],[0,0,0]]
soma_pares=0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]=int(input(f'Digite um número para [{l},{c}]: '))
        if matriz[l][c] %2==0:
            soma_pares+=matriz[l][c]
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()
print('-='*30)
print(f'A soma de todos valores pares foi: {soma_pares}')
print(f'A soma dos valores da terceira coluna foi: {matriz[0][2]+matriz[1][2]+matriz[2][2]}')
print(f'O maior valor da segunda linha: {max(matriz[1])}')
print('-='*30)