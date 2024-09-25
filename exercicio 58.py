from random import randint
p = 0
r = 1
while p != r:
    p = int(input('tente adivinhar o numero de 1 a 10:'))
    r = randint(0, 10)
    if r == p:
        print(f'você acertou,parabéns, o resultado foi {r}')
    else:
        print(f'você errou, o resultado foi {r}, mais sorte na proxima')
