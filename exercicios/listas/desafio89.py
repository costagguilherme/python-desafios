lista = []
m = []
cont = 0
while True:
    nome = str(input('NOME: '))
    n1 = int(input('NOTA 1: '))
    n2 = int(input('NOTA 2: '))
    cont = cont + 1
    next = str(input('QUER CONTINUAR? S ou N: ')).upper().strip()
    while next != 'S' and next != 'N':
        next = str(input('QUER CONTINUAR? S ou N: ')).upper().strip()
    if next == 'N':
        print('PROGRAMA ENCERRADO')
        break

c = 0
while c <= cont:
    lista.append([nome, n1, n2])
    m.append((n1 + n2) / 2)


print(lista)
print(m)