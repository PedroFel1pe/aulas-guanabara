n1 = int(input('informe um numero inteiro:'))
n2 = int(input('informe o segundo numero:'))
if n1 > n2:
    print(f'o primeiro numero {n1} é maior que o segundo numero {n2}')
elif n2 > n1:
    print(f'o segundo numero {n2} é maior que o primeiro {n1}')
else:
    print(f'os dois números possuem o mesmo valor {n1}')
