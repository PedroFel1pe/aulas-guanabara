f = str(input('digite uma frase:')).strip().upper()
print(f.count('A'))
print('a primeira letra (a) foi encontrada na posição {}'.format(f.find('A') + 1))
print('e a ultima na posição {}'.format(f.rfind('A') + 1))