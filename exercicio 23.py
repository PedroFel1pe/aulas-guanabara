n = int(input('digite un numero de 4 digitos:'))
#print('unidade é {}'.format(n[3]))
#print('dezena é {}'.format(n[2]))
#print('centena é {}'.format(n[1]))
#print('milhar é {}'.format(n[0]))
#dessa forma dara erro se colocar numeros q n forem de 4 digitos
print('unidade é {}'.format( n//1 % 10))
print('dezena é {}'.format(n//10 % 10))
print('centena é {}'.format(n//100 % 10))
print('milhar é {}'.format(n//1000 % 10))