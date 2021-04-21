n = int(input('Qual a velocidade do carro em km/h? '))
multa = (n - 80) * 7
if n > 80:
    print('Você foi multado por excesso de velocidade')
    print(f'O valor da multa será de {multa}R$ !')
