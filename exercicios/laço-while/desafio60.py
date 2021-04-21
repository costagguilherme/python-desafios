n = int(input('ESCOLHA UM NÚMERO: '))
r = 1
count = 1
print(f'{n}! = ', end='')
while count <= n:
    print(f'{count} ', end='')
    r = r * count
    count = count + 1
    print(' x ' if count <= n else '= ', end='')
print(r)
