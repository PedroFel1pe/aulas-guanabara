from datetime import date
atual = date.today().year
idade = int(input('informe seu ano de nascimento:'))
a = atual - idade
b = a - 18
c = 18 - a
if a < 18:
    print(f'você devera se alistar daqui {c} anos')
elif a > 18:
    print(f'você deveria ter se alistado a {b} anos atrás')
else:
    print('você deve se alistar este ano')
