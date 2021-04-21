nome = str(input('NOME DO JOGADOR: ')).upper()
print('=-'*30)
p = int(input(f'QUANTAS PARTIDAS {nome} JOGOU? '))
print('=-'*30)
soma = 0
gols = []
info = {}
for c in range(0,p):
    gol = (int(input(f'GOLS NA PARTIDA {c}:  ')))
    gols.append(gol)
    soma = soma + gol

info['NOME'] = nome
info['GOLS'] = gols
info['TOTAL'] = soma
print(info)
print('=-'*30)
for k, v in info.items():
    print(f'O CRITÉRIO {k} tem valor {v}.')
print('=-'*30)
print(f'O JOGADOR {nome} JOGOU {p} PARTIDAS.')
print('=-'*30)
for i, v in enumerate(info['GOLS']):
    print(f'NA PARTIDA {i}, fez {v} GOLS')
print('=-'*30)
print(f'TOTAL DE {soma} GOLS')