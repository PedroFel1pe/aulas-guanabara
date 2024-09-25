print('calculo do IMC, Índice Massa Corpórea')
# peso = weight e altura = height
weight = float(input('qual o seu peso atualmente?KG'))
height = float(input('qual a sua altura em metros?'))
# outra forma de calcular ao quadrado é (height ** 2)
imc = weight / (height * height)
if imc < 18.5:
    print(f'abaixo do peso,IMC de {imc:.2f}')
elif 18.5 <= imc < 25:
    print(f'peso ideal,IMC de {imc:.2f}')
elif 25 <= imc < 30:
    print(f'sobre peso,IMC de {imc:.2f}')
elif 30 <= imc < 40:
    print(f'obesidade.IMC de {imc:.2f}')
else:
    print(f'obesidade mórbida,IMC de {imc:.2f}')
