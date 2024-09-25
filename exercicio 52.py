num = int(input('informe um valor para vermos se ele é um numero primo = '))
total = 0
# maneira que eu fiz não está errado, mas também não esta certo, tinha que ter utilizado o for
# if '2' == num or num == '3':
#    print('é um numero primo')
# elif num % 2 == 0 or num % 3 == 0:
#    print('este é um numero composto')
# else:
#    print('ele é um numero primo')
for c in range(1, num + 1):
    if num % c == 0:
        print(f'\033[34m{c}', end=' ')
        total += 1
    else:
        print(f'\033[31m{c}', end=' ')
if total == 2:
    print(f'\n\33[m ele é um numero primo, pois ele foi divisível apenas {total}')
else:
    print(f'\n\33[m ele é um numero composto, pois ele foi divisível {total}')
