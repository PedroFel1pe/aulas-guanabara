peso = []
for c in range(1,6):
    pesos = float(input(f'peso da {c}° pessoa: '))
    peso.append(pesos)
print(f'o maior peso foi de {max(peso)} e o de menor foi de {min(peso)}.')
