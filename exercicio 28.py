from random import randint
p = int(input('tente adivinhar o numero de 1 a 10:'))
r = randint(0,10)
if r == p:
    print('você acertou,parabéns')
else:
    print('você errou, mais sorte na proxima')
print('o resultado foi {}'.format(r))
