n = int(input('Quer visualizar a tabuada de qual valor: '))
cont = 1
while True:
    if n < 0:
        break
    if n >= 0 and 1 <= cont <=10:
        print(f'{n} x {cont} = {n * cont}')
        cont = cont + 1
    if cont > 10:
        cont = 1
        n = int(input('Quer visualizar a tabuada de qual valor: '))
        if n < 0:
            break
        cont = cont + 1
        print(f'{n} x {cont} = {n * cont}')