info = {}
nome = str(input('NOME: '))
nasc = int(input('ANO DE NASCIMENTO: '))
idade = 2020 - nasc
cart = int(input('CARTEIRA DE TRABALHO (0 Se não tiver): '))
info['NOME'] = nome
info['IDADE'] = idade
info['NASCIMENTO'] = nasc
info['CTPS'] = cart
if cart == 0:
    for k, v in info.items():
        print(f'{k} = {v}')
if cart > 0:
    contrat = int(input('ANO DE CONTRATAÇÃO: '))
    sal = int(input('SALÁRIO: R$ '))
    contri = 2020 - contrat
    anoaposent = 2020 + (35 - contri)
    idadeaposent = idade + (anoaposent - 2020)
    info['ANO DE CONTRATAÇÃO'] = contrat
    info['SALÁRIO'] = sal
    info['APOSENTADORIA'] = idadeaposent
    for k, v in info.items():
        print(f'{k} = {v}')