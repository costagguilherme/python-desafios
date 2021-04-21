print('=====  CAMPO DE REGISTROS  =====')
print('=-' * 25)
i = 0
contmais18 = 0
conthomem = 0
contmenos20 = 0


while True:
    i = int(input('INFORME A IDADE: '))
    s = str(input('INFORME O SEXO (M ou F): ')).upper().strip()
    print('=-' * 25)

    if i > 18:
        contmais18 = contmais18 + 1

    if s == 'F':
        if i < 20:
            contmenos20 = contmenos20 + 1
    if s == 'M':
        conthomem = conthomem + 1

    if s == 'M' or s == 'F':
        print('REGISTRADO COM SUCESSO!')
        print('=-'*25)


    if s != 'M' and s != 'F':
        print('OPÇÃO INVÁLIDA')
        while s != 'M' and s != 'F':
            s = str(input('INFORME O SEXO (M ou F): ')).upper().strip()
            if s == 'M':
                conthomem = conthomem + 1

        print('REGISTRADO COM SUCESSO!')
        print('=-'*25)


    next = str(input('QUER CONTINUAR? (S ou N): '))

    if next == 'N':
        print('PROGRAMA ENCERRADO!')
        break

    if next == 'S':
        print('=-'*25)

    if next != 'S' and next != 'N':
        print('OPÇÃO INVÁLIDA')
        while next != 'S' and next != 'N':
            next = str(input('QUER CONTINUAR? (S ou N): '))

print('=-'*25)
print(f'{contmais18} PESSOAS TÊM MAIS DE 18 ANOS.')
print(f'{conthomem} HOMENS FORAM CADASTRADOS.')
print(f'{contmenos20} MULHERES TÊM MENOS DE 20 ANOS.')