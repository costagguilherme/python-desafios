import random
print('======PAR OU IMPAR======')
npc = random.randint(0,10)
cont = 0
while True:
    j = str(input('ESCOLHA SUA JOGADA P ou I: ')).strip().upper()
    print('-=' * 30)

    if j != 'P' and j != 'I':
        print('OPÇÃO INVÁLIDA')
        print('-=' * 30)

        break

    n = int(input('ESCOLHA UM NÚMERO (0 á 10) PARA SUA JOGADA: '))
    print('-=' * 30)
    print(f'VOCÊ JOGOU {n} E SEU OPONENTE {npc}')
    print(f'RESULTADO = {n + npc}')
    print('-=' * 30)

    if j == 'P':
        pc = 'I'

    if j == 'I':
        pc = 'P'

    if (n + npc) % 2 == 0:
        if j == 'P':
            print('VOCÊ VENCEU!')
            cont = cont + 1
            print('JOGUE NOVAMENTE...')
            print('-=' * 30)
        if j == 'I':
            print('VOCÊ PERDEU!')
            break

    if (n + npc) % 2 != 0:
        if j == 'P':
            print('VOCÊ PERDEU!')
            break
        if j == 'I':
            print('VOCÊ VENCEU!')
            cont = cont + 1
            print('JOGUE NOVAMENTE...')
            print('-=' * 30)

print(f'VOCÊ VENCEU {cont} VEZES!')