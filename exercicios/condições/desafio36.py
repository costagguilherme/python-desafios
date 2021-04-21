casa = int(input('Qual o valor da casa em reais? '))
sal = int(input('Qual o valor do seu salário em reais? '))
anos = int(input('Em quantos anos você irá pagar a casa? '))
meses = anos * 12
prest = casa / meses
max = 0.3 * sal
if prest > max:
    print('EMPRESTIMO NEGADO')
elif prest <=max:
    print('VOCÊ PODE PERDIR O EMPRESTIMO')
