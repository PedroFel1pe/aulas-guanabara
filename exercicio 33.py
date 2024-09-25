n1 = int(input('informe um numero:'))
n2 = int(input('digite outro:'))
n3 = int(input('digite mais um numero:'))
m = n1
if n2 < n1 and n2 < n3:
    m = n2
if n3 < n1 and n3 < n2:
    m = n3
M = n1
if n2 > n1 and n2 > n3:
    M = n2
if n3 > n1 and n3 > n2:
    M = n3
print('o menor numero é {}'.format(m))
print('o maior numero é {}'.format(M))
