# fazer a soma dos números impares de 1 a 500 ,múltiplos de 3
soma = 0
contador = 0
for par in range(1, 500, 2):
    if par % 3 == 0:
        # tem estas duas maneiras de realizar esse tipo de código
        soma += par
        contador = contador + 1
print(f'a soma dos valores é {soma}')
print(f'foi feita a soma de {contador} números')
