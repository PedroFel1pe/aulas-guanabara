print('informe sua nota tirada das duas atividades valendo 5pts cada uma')
n1 = float(input('resultado da primeira atividade:'))
n2 = float(input('resultado da segunda atividade:'))
total = (n1 + n2) / 2
if total >= 7:
    print(f'parabens você foi aprovado com {total}pts')
elif total <= 5:
    print(f'infelizmente você foi reprovado, á média para aprovação é de 7,00 pts você foi com {total}pts')
else:
    print(f'você esta de recuperação, com {total}')
