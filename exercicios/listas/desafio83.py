
a = input('DIGITE A EXPRESSÃO: ')
b = (list(a))
if b.count('(') == b.count(')'):
    print('EXPRESSÃO VÁLIDA')
if b.count('(') != b.count(')'):
    print('EXPRESSÃO INVÁLIDA')