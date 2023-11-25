"""Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero
até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso."""

tupla=('zero','um','dois','três','quatro','cinco',' seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze' ,'treze', 'catorze','quinze','dezesseis','dezessete','dezoito', 'dezenove','vinte')
chave=0
while True:
    num=int(input('Digite número entre (0 e 20): ou digite [999] para sair!: '))
    if num == 999:
        break
    if num < 0 or num >20:
        print("Tente novamente, Digite um número entre (0 e 20) ou digite [999] para sair!: ")
    else:
        print(f"Você digitou o número {tupla[num]}.")
