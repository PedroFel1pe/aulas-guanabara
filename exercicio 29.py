v = float(input('informe a velocidade em que você se encontrava:'))
m = (v-80)*7
if v <= 80:
    print('você estava no limite da velocidade')
else:
    print('você levou uma multa de {:.2f}'.format(m))
    