ano = int(input('Qual seu ano de nascimento? '))
idade = 2020 - ano
n1 = 18 - idade
n2 = idade - 18
if idade < 18:
    print(f'Faltam {n1} anos para você se alistar.')
elif idade == 18:
    print('Você deve se alistar ainda este ano!')
elif idade > 18:
    print(f'Já era para você ter se alistado há {n2} anos')