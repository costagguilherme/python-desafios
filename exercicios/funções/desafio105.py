def notas(*n, sit=False):
    valores = {}
    valores['Quantidade'] = len(n)
    valores['maior'] = max(n)
    valores['menor'] = min(n)
    valores['media'] = sum(n) / len(n)
    if sit:
        if valores['media'] < 6:
            valores['Situação'] = 'Sofrível'
        if 6 <= valores['media'] < 7:
            valores['Situação'] = 'Razoável'
        if valores['media'] >= 7:
            valores['Situação'] = 'Bom'
    return valores


print(notas(8, 9, 7, 6, 10, sit=True))