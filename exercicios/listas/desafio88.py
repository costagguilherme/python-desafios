import random
print('PALPITES ALEATÓRIO MEGA - SENA')
print('-='*30)
jogo = int(input('QUANTOS JOGOS VOCÊ QUER GERAR? '))
print('-='*30)
print('OS JOGOS GERADOS FORAM: ')
print('-='*30)

palpites = []
cont = 0
for c in range(0, jogo):
    palpites.append([random.randint(1,60), random.randint(1,60), random.randint(1,60), random.randint(1,60), random.randint(1,60), random.randint(1,60)])
    print(palpites)
    palpites.clear()