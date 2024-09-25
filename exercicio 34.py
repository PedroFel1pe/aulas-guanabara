s = float(input('informe seu salario R$:'))
if s > 1250.00:
    print('seu salario sera de R${:.2f}'.format(s/100*10+s))
else:
    print('seu salario sera de R${:.2f}'.format(s/100*15+s))
# outra forma de calcular porcentagem é o numero * a porcentagem q quero / 100
