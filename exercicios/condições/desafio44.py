p = float(input('INFORME O VALOR DO PRODUTO R$'))
a = p - (0.1 * p)
b = p - (0.05 * p)
pcomjuros = p + ( p * 0.2)
print('Qual a opção de pagamento ?')
print(''' OPÇÕES DE PAGAMENTO
[ 1 ] Á vista em dinheiro/cheque.
[ 2 ] Á vista no cartão.
[ 3 ] Em até 2x no cartão.
[ 4 ] 3x ou mais no cartão. ''')
e = int(input('Qual a sua opção?'))
if e == 1:
    print(f'O valor do produto ficará R${a} ')
elif e == 2:
    print(f'O valor do produtado ficará R${b}')
elif e == 3:
    print(f'O preço do produto se manterá em R${p}')
elif e == 4:
    vezes = int(input('Em quantas vezes você quer parcelar? '))
    print(f'O preço do produto será R${pcomjuros}')
    prest = pcomjuros / vezes
    print(f'As prestações serão no valor de R${prest} por mês em {vezes} meses')
else:
    print('OPÇÃO INVALIDA DE PAGAMENTO, TENTE NOVAMENTE!')