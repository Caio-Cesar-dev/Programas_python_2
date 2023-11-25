"""Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para
cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo."""
mult=0
cont=1
while True:
    print('-'*35)
    tab=int(input("Quer ver a tabuada de qual valor: "))
    print('-'*35)
    if tab < 0:
        break
    for cont in range(0,11,1):
        print(f"{tab} x {cont} = {tab * cont}")
        cont+=1
print("PROGRAMA TABUADA ENCERRADO. Volte Sempre!!")