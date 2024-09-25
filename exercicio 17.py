from math import hypot
co = float(input('digite o cateto oposto:'))
ca = float(input('o cateto adjacente:'))
h = hypot(co, ca)
print('a hipotenusa é {} '.format(h))
