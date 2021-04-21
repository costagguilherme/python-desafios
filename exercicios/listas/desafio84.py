info = []
dados =[]
cont= 0
while True:
    info.append(str(input('INFORME UM NOME: ')))
    info.append(int(input('INFORME UM PESO: ')))
    dados.append(info[:])
    info.clear()
    cont = cont + 1

    next = str(input('QUER CONTINUAR? S ou N: ')).upper().strip()
    while next != 'S' and next != 'N':
        next = str(input('QUER CONTINUAR? S ou N: ')).upper().strip()
    if next == 'N':
        print('PROGRAMA ENCERRADO')
        break

peso = []
nome = []
nomemaior = 0
nomemenor = 0
geral = []
for c in range(0, len(dados)):
    peso.append(dados[c][1])
    maior = max(peso)
    menor = min(peso)
    nome.append(dados[c][0])
    geral.append(dados[c][0])
    geral.append(dados[c][1])
    if dados[c][1] == maior:
        nomemaior = dados[c][0]
    if dados[c][1] == menor:
        nomemenor = dados[c][0]
print('--'*20)
print(f'O MENOR PESO É {menor}KG DE {nomemenor}')
print('--'*20)
print(f'O MAIOR PESO É {maior}KG {nomemaior}')
print('--'*20)
print(f'{cont} PESSOAS FORAM CADASTRADAS.')