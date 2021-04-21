import random
cont = 0
print('=-' * 20)
print('PEDRA PAPEL TESOURA')
print('=-' * 20)
print(''' ESCOLHA UMA OPÇÃO:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA ''')
pc = random.randint(1,3)
print('=-' * 20)
while True:
    vc = int(input('ESCOLHA UMA DAS TRÊS OPÇÕES: '))
    print('=-' * 20)
    if pc != vc:
        if pc == 1 and vc == 2:
            print(f'Seu oponente escolheu PEDRA e você escolheu PAPEL.')
            print('VOCÊ VENCEU!')
            cont = cont + 1
        elif pc == 1 and vc == 3:
            print('Seu opnonente escolheu PEDRA e você escolheu TESOURA.')
            #VOCÊ PERDEU
            break

        elif pc == 2 and vc == 1:
            print('Seu oponente escolheu PAPEL e você escolheu PEDRA.')
            #VOCÊ PERDEU
            break
        elif pc == 2 and vc == 3:
            print('Seu oponente escolheu PAPEL e você escolheu TESOURA.')
            print('VOCÊ VENCEU!')
            cont = cont + 1
        elif pc == 3 and vc == 1:
            print('Seu oponente escolheu TESOURA e você escolheu PEDRA.')
            print('VOCÊ VENCEU!')
            cont = cont + 1
        elif pc == 3 and vc == 2:
            print('Seu oponente escolheu TESOURA e você escolheu PAPEL.')
            #VOCÊ PERDEU
            break
        print('=-' * 20)

    elif pc == vc:
        if pc == vc == 1:
            print('Empate, ambos escolheram PEDRA.')
        elif pc == vc == 2:
            print('Empate, ambos escolheram PAPEL.')
        elif pc == vc == 3:
            print('Empate, ambos escolheram TESOURA,')
        print('=-' * 20)

print('=-' * 20)
print(f'VOCÊ PERDEU APÓS {cont} VITÓRIAS!')