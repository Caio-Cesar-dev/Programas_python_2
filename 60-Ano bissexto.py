"""Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto."""
from datetime import date
print()

ano=int(input("\033[7;30;45mQual ano você que analisar? ou coloque 0 para analisar o ano atual!: \033[m"))
if ano == 0:
    ano=date.today().year         # busca o ano atual em que a máquina esta configurada
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 ==0:
    print("\033[1;34mO ano {} é BISSEXTO".format(ano))
else:
    print("\033[1;31mO ano {} não é BISSEXTO".format(ano))