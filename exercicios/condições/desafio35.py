a = int(input('Qual o comprimento da reta a? '))
b = int(input('Qual o comprimento da reta b? '))
c = int(input('Qual o comprimento da reta c? '))
if b + c > a > b - c:
    print('É possível que se  forme um triângulo com essas retas ')
else:
    print('Não é possivel que se forme um triângulo com essas retas ')