"""Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando
 o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi
 a soma entre eles (desconsiderando o flag)."""

num1=cont=soma= 0 # quando todas variaveis iniciam com o mesmo valor podemos fazer assim
num1=int(input("digite um número [999 para parar]: ")) # para entrar no loop já comarando o flag
while num1 != 999:
    soma =soma + num1
    cont += 1
    num1 = int(input("digite um número [999 para parar]: ")) # no final do ciclo para ser comparado caso seja o flag não entra na soma nem na contágem
print(f"Voce digitou {cont} numeros e a soma entre eles foi {soma} ")
