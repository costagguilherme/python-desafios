valor = int(input('INFORME O VALOR QUE VOCÊ QUER SACAR: '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total = total - ced
        totced = totced + 1
    elif total < ced:
        print(f'TOTAL DE {totced} NOTA de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0

        if total == 0:
            break