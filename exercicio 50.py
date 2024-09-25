s = 0
cont = 0
for c in range(1, 7):
    num = int(input('digite um numero inteiro: '))
    if num % 2 == 0:
        s += num
        cont += 1
print(f'o somatório dos {cont} valores pares foi de {s}')
