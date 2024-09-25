from random import shuffle
n1 = input('primeiro nome:')
n2 = input('segundo nome:')
n3 = input('terceiro nome:')
n4 = input('quarto nome:')
l = [n1, n2, n3, n4]
shuffle(l)
print('a ordem sera {}'.format(l))
