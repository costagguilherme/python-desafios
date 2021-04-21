f = ('LINUX', 'WINDOWS', 'COMPUTADOR', 'NOTEBOOK', 'PYTHON')
for p in f:
    print(f'\nNa palavra {p} temos: ', end='')
    for letra in p:
        if letra in 'AEIOU':
            print(letra, end=' ')