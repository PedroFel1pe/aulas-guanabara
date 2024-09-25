print('---+' * 10)
print('seja bem vindo, vamos medir quanto de tinta você precisara para pintar a parede!!!')
a = float(input('informe a altura da parede:'))
l = float(input('informe a largura da parede:'))
s = a * l
print('a sua parede tem {:.2f} x {:.2f} logo ela possui {}m²'.format(a, l, s))
print('você ira precisar de {:.2f}L de tinta'.format(s / 2))
print('---+' * 10)
