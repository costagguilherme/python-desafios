from time import sleep

def ajuda(msg):
    help(msg)


def title(titulo):
    print('~' * (len(titulo)))
    print(titulo)
    print('~' * (len(titulo)))


while True:
    title('SISTEMA DE AJUDA')
    a = input('Função ou biblioteca: ')
    sleep(1)
    b = f'FUNÇÃO {a.upper()}'
    title(b)
    ajuda(a)
    if a.upper() == 'FIM':
        break
print(b)