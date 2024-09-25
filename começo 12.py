prod = float(input('qual o valor do produto:R$'))
valor = prod / 100 * 95
print('este produto esta com 5% de promoção, então ele deixara de valer R${:.2f} para valer R${:.2f}'.format(prod, valor))
#outra forma de calcular porcentagem é o numero x porcentagem / por 100 - o numero
