import random
n1 = input('1° nome a ser sorteado-')
n2 = input('2° nome a ser sorteado-')
n3 = input('3° nome a ser sorteado-')
n4 = input('4° nome a ser sorteado-')
l = [n1, n2, n3, n4]
e = random.choice(l)
print('o sorteado sera {}'.format((e)))