l1 = float(input('digite o valor da reta :'))
l2 = float(input('digite a segunda reta:'))
l3 = float(input('digite a ultima reta:'))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('ele pode ser um triangulo, ', end='')
    if l1 == l2 == l3:
        print(f'E este é um triângulo equilátero com todos os lados medindo {l1}')
    elif l1 == l2 or l2 == l3 or l1 == l3:
        print(f'E este é um triângulo isósceles que possui dois lados iguais e um diferente')
    else:
        print('este é um triângulo escaleno que possui todos os lados diferentes do outro ')

else:
    print('ele não pode ser um triangulo')
