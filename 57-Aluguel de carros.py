"""Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
e R$0,15 por Km rodado."""
print(100*'-')
print("*****Bem vindos à nossa loja de carros!!*****")
print()
km=int(input("Por favor, nos informe a kilometragem percorrida: Km "))
dias=int(input("Informe a quantidade de dias com o veiculos alugado: "))

print()
print("\033[1;33mO valor a ser pago é de {:.2f} Reais".format((km*0.15)+(dias*60)))

