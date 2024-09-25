import math
a = float(input('digite um angulo:'))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print('o valor de seno é {:.2f}, o cosseno é de{:.2f} e a tangente é{:.2f}'.format(s, c, t))
