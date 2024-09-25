print('você sabia que existe varias formas de representar um numero?')
n = int(input('vamos conhecer alguns desses outros modos,primeiramente informe um numero:'))
tipo = str(input('qual tipo de forma você quer ver? binario, octal ou hexadecimal:')).strip().lower()
binario = bin(n)
octal = oct(n)
hexadecimal = hex(n)
if tipo == 'binario':
    print(f'este tipo é utilizado principalmente na computação,sendo {binario[2:]} o valor de {n}')
elif tipo == 'octal':
    print(f'o valor {n} em octal sera de {octal[2:]}')
else:
    print(f'o valor {n} em hexadecimal é de {hexadecimal[2:]}')
