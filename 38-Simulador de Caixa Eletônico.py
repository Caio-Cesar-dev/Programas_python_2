"""Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão
entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1."""
print('='*30)
print('{:^30}'.format("BANCO MATTA"))
print('='*30)
valor=int(input("Qual valor deseja sacar? R$ "))
total=valor
ced=50
totced=0
while True:
    if total>=ced:
        total = total - ced
        totced+=1
    else:
        if totced > 0: # só escreve se o total de cedula for maior que zero
            print(f"Total de {totced} cedula de R$ {ced}")
        if ced ==50:
            ced=20
        elif ced ==20:
            ced=10
        elif ced ==10:
            ced=1
        totced = 0 # zera a contagem de cédulas para o proximo loop
        if total ==0:
            break
print('='*30)
print("Volte sempre ao Banco MATTA! Tenha um bom dia!")


