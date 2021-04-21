def voto(n):
    if (2020 - n) < 18:
        return print('VOTO NÃO É OBRIGATÓRIO')
    if 18 <= (2020 - n) < 65:
        return print('VOTO OBRIGATÓRIO')
    if (2020 - n) >= 65:
        print('VOTO OPCIONAL')
d = int(input('INFORME O ANO DE NASCIMENTO: '))
voto(d)