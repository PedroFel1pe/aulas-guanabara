l1 = float(input('digite o valor da reta :'))
l2 = float(input('digite a segunda reta:'))
l3 = float(input('digite a ultima reta:'))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 +l2:
    print('\033[;30m ele pode ser um triangulo')
else:
    print('ele não pode ser um triangulo')
