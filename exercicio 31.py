km = float(input('quantos km voçê percorreu?'))
if km <= 200:
    print('você ira pagar R${:.2f} de passagem'.format(km * 0.50))
else:
    print('você ira pagar R${:.2f} de passagem'.format(km * 0.45))