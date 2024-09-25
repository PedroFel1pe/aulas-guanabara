from datetime import date
ano = date.today().year
nascimento = int(input('informe seu ano de nascimento para indicarmos a sua categoria:'))
idade = ano - nascimento
print(f'o nadador tem {idade} logo sua categoria sera')
if idade <= 9:
    print('mirim')
elif 10 <= idade <= 14:
    print(f'infantil ')
elif 15 <= idade <= 19:
    print('junior')
elif idade == 20:
    print('senior')
else:
    print('master')
