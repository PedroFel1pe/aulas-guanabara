valor = float(input('valor da compra:'))
print('''opções de pagamento 
[1]a vista no dinheiro ou cheque
[2]no cartão
[3]2x no cartão 
[4]3x ou mais no cartão''')
print('pagando á vista voçê tera desconto já parcelado tera uma taxa de juros')
modoDePagamento = str(input('como voçê deseja pagar?'))
if '1' == modoDePagamento:
    print(f'Voçê tera um desconto de 10%, então de R${valor} ficara por R${(valor/100)*90:.2f}')
elif modoDePagamento == '2':
    print(f'Voçê tera um desconto de 5%, então de R${valor} ficara por R${(valor/100)*95:.2f}')
elif modoDePagamento == '3':
    print(f'Sua compra ficara R${valor:.2f}')
else:
    print(f'voçê tera uma taxa de 20% de juros, de R${valor} ficara por R${(valor/100)*20+valor:.2f}')
