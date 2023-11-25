"""Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense."""#vou substituir pelo bahia

times=('Flamengo','Internacional','Atlético-MG','São Paulo','Fluminense','Grêmio','Palmeiras','Santos','Athletico-PR',
       'Bragantino','Ceará','Corinthians','Atlético-GO','Bahia','Sport','Fortaleza','Vasco','Goiás','Coritiba','Botafogo')
print("Times do brasileirão 2020: ",times)
print('=-'*40)
print(f"Os primeiros colocados são: {times[0:5]}")
print('=-'*40)
print(f"Os quatro últimos colocados{times[-4:]} ")
print('=-'*40)
print(f"O bahia ficou em {times.index('Bahia')+1}º colocado.")
print('=-'*40)
print("Em ordem alfabetica:",sorted(times))