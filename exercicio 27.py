n = str(input('digite o seu nome:')).strip()
l = n.split()
print('o seu primeiro nome é {}'.format(l[0]))
print('e o seu ultimo nome é {}'.format(l[len(l)-1]))