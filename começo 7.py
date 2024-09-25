n = float(input('informe um valor:'))
print('o dobro de', n, 'equivale a \033[;4;32m{}\033[;m'.format(n * 2))
print('a metade de', n, 'equivale a \033[4;31m{}\033[;m'.format(n / 2))
print('a raiz de', n, 'equivale a \033[;4;34m{}'.format(n ** (1 / 2)))
# ** significa elevado
