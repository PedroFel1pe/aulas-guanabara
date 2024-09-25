fator = int(input('digite um numero para fatorear:'))
multiplicação = 1
while fator != 0:
    multiplicação *= fator
    print(f'{fator}')
    fator -= 1
print(f'O fatoreamento dele é {multiplicação}')
