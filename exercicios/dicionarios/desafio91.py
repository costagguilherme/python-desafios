from random import randint
from time import sleep
from operator import itemgetter
jogadas = {}
for c in range(1,5):
    a = randint(1, 6)
    print(f'O PLAYER {c} tirou {a} no dado')
    jogadas[f'PLAYER {c}'] = a
    sleep(0.5)
ranking = []
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
print('=-'*30)
for c in range(0,4):
    sleep(0.5)
    print(f' O {ranking[c][0]} ficou em {c + 1}° com {ranking[c][1]}')