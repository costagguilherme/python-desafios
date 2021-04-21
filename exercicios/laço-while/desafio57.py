sexo = str(input('Informe seu sexo > M ou F: ')).upper()[0].strip()

while sexo != 'M' and sexo != 'F':
    print('OPÇÃO INVÁLIDA')
    sexo = str(input('Informe seu sexo novamente > M ou F: ')).upper().strip()

if sexo == 'M' or sexo == 'F':
    print('Sexo registrado')