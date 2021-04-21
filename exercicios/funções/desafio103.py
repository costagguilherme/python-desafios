def ficha(nome='<desconhecido>',gol=0):
    print(f'O jogador {nome} fez {gol} gol(s)')

n = str(input('Informe o nome: ')).strip()
g = str(input('Informe a quantidade de gols: ')).strip()

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n == '':
    ficha(gol=g)
else:
    ficha(n,g)