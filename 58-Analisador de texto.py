"""Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome."""

nome=str(input("Digite o seu nome completo: ")).strip() # o strip já elimina os espaços antes e depois
print("Seu nome em Maiúculas: ",nome.upper())
print("O seu nome em minúsculas: ",nome.lower())
print("Seu nome tem ao todo {} letras ".format(len(nome) - nome.count(' '))) #com a função len retornamos o total de
#simbolos incluindo os espaços, subtraimos com o count os espaços existentes.
print("Seu primeiro nome tem {}".format(nome.find(' '))) #O find mostra o inicio que inicia a posição do espaço
#outra maneira de fazer o ultimo item
separa=nome.split()
print("O seu primeiro nome é {} e ele tem {} letras". format(separa[0],len(separa[0])))
