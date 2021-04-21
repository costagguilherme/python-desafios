galera = []
pessoa = {}
mulheres = {}
soma = 0
nomemedia = 0
while True:
    nome = str(input('NOME: '))
    while True:
        sexo = str(input('SEXO, M ou F: ')).upper()
        if sexo in 'MF':
            break
        else:
            print('ERRO')

    idade = int(input('IDADE: '))
    soma = soma + idade
    pessoa['NOME'] = nome
    pessoa['SEXO'] = sexo
    pessoa['IDADE'] = idade
    galera.append(pessoa.copy())

    next = str(input('QUER CONTINUAR? S ou N: ')).upper().strip()
    while next != 'S' and next != 'N':
        next = str(input('QUER CONTINUAR? S ou N: ')).upper().strip()
    if next == 'N':
        print('PROGRAMA ENCERRADO')
        break
print(galera)
print(f'{len(galera)} PESSOAS FORAM CADASTRADAS.')
print(f'MÉDIA DE IDADE = {soma / len(galera)}')
for p in galera:
    if p['SEXO'] in 'Ff':
        print('AS MULHERES CADASTRADAS FORAM: ', end='')
        print(f'{p["NOME"]}', end='')
        print('')
for p in galera:
    if p['IDADE'] >= (soma / len(galera)):
        print('  ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
            print('', end='')
print('ENCERRADO')