print('=-' * 40)
print('ANALISADOR COMPLETO')
print('=-' * 40)
somaidade = 0
menorque20 = 0
totmulher = 0
tothomem = 0
idadehomem = 0
idadevelho = []
nomevelho = 0
maior = 0

for c in range(1, 5):
    n = str(input('[NOME]: ')).upper().strip()
    i = int(input('[IDADE]: '))
    s = str(input('[SEXO] M ou F: ')).upper().strip()
    somaidade = somaidade + i
    media = somaidade / 4

    if s == 'M':
        idadadehomem = idadehomem + i
        idadevelho = idadevelho + [i]
        maior = max(idadevelho)
        tothomem = tothomem + 1
        if i == maior:
            nomevelho = n


    elif s == 'F':
        totmulher = totmulher + 1

    if s == 'F' and i < 20:
        menorque20 = menorque20 + 1

print('=-' * 40)

if totmulher + tothomem < 4:
    print('PREENCHA NOVAMENTE AS INFORMAÇÕES CORRETAMENTE PARA PROSEGUIR.')

if totmulher + tothomem == 4:
    if totmulher > 0 and tothomem > 0:
        print(f'A média das idades das pessoas é: {media:.2f} anos')
        print('=-' * 40)
        print(f'No grupo possui um total de {totmulher} mulheres.')
        print(f'{menorque20} mulheres possuem menos de 20 anos.')
        print('=-' * 40)
        print(f'O homem mais velho deste grupo é {nomevelho} com {maior} anos.')

    if tothomem > 0 and totmulher == 0:
        print(f'A média das idades das pessoas é: {media:.2f} anos')
        print('=-' * 40)
        print(f'O homem mais velho deste grupo é {nomevelho} com {maior} anos.')
        print('=-' * 40)
        print('Não há mulheres no grupo.')

    if totmulher > 0 and tothomem == 0:
        print(f'A média das idades das pessoas é: {media:.2f} anos')
        print('=-' * 40)
        print(f'No grupo possui um total de {totmulher} mulheres.')
        print(f'{menorque20} mulheres possuem menos de 20 anos.')
        print('=-' * 40)
        print('Não há homens no grupo')