a1 = int(input('INFORME O 1° TERMO DA P.A: '))
r = int(input('INFORME A RAZÃO DA P.A: '))
cont = 0
dez = 10
while cont < dez:
    if cont != dez:
        print(f'{a1}', end=' -> ')
        a1 = a1 + r
        cont = cont + 1

    if cont == dez:
        print('FIM')
        mais = int(input('Quantos mais termos você quer visualizar: '))
        dez = dez + mais
        if mais == 0:
            print('PROGRAMA ENCERRADO')

print(f'A P.A se encerrou com {cont} termos.')