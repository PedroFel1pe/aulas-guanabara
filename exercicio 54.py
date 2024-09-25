from datetime import date
atual = date.today().year
print('vamos ver quem ja é maior de idade aqui')
contagemDeMaior = 0
contagemDeMenor = 0
for c in range(0, 7):
    nascimento = int(input('qual o seu ano de nascimento? '))
    idade = atual - nascimento
    if idade >= 21:
        print(f'voçê ja é de maior, com {idade} de idade.')
        contagemDeMaior += 1
        contagemDeMenor = 7 - contagemDeMaior
    else:
        print(f'voçê é de menor ainda, com {idade} de idade.')

print(f'temos {contagemDeMaior} de maiores e {contagemDeMenor} de menores.')

