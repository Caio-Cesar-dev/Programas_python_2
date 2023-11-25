"""Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo."""
from random import randint
print("-="*20)
print("VAMOS JOGAR PAR OU ÍMPAR")
print('-='*20)

cont=0
while True:
    computer = randint(0, 10)
    jogador=int(input("Diga um valor [de 1 a 10]: "))
    p_i=str(input("Par ou Impar: [P/I]: ")).upper()
    print('-'*40)
    if p_i == 'P':
        if (computer + jogador)%2==0:
            print(f"O computador jogou {computer} e você jogou {jogador} total {computer+jogador} é PAR, Você VENCEU!")
        else:
            if (computer + jogador) % 2 != 0:
                print(f"O computador jogou {computer} e você jogou {jogador} total {computer+jogador} é IMPAR. Você PERDEU!")
                break
    if p_i == 'I':
        if (computer + jogador)%2==0:
            print(f"O computador jogou {computer} e você jogou {jogador} total {computer+jogador} é PAR. Você PERDEU!")
            break
        else:
            if (computer + jogador) % 2 != 0:
                print(f"O computador jogou {computer} e você jogou {jogador} total {computer+jogador} é IMPAR. Você VENCEU!")
    print('-'*40)
    print("Vamos jogar novamente!!")
    cont += 1
print(f"GAME OVER! Você venceu {cont} vezes.")