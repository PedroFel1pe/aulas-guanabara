print('realize seu empréstimo aqui, primeiramente precissamos de seus dados, então vamos começar!!!!!')
print('-//-'*10)
nome = str(input('seu nome completo:')).strip()
valor = int(input('qual o valor do empréstimo:'))
salario = int(input('qual o seu salário:R$'))
tempo = int(input('em quantos anos você ira pagar:'))
vm = valor / tempo / 12
ps = salario / 100 * 30
if vm < ps:
    print('Seu empréstimo foi liberado com sucesso!!. Ele sera do valor de R${:.2f}'.format(vm))
elif vm == ps:
    print(f"Seu empréstimo foi liberado, mas cuidado que o valor da mensalidade de R${vm:.2f} equivale a 30% do seu salario!!")
else:
    print('infelizmente não foi possivel realizar o empréstimo, pois a mensalidade ultrapassa o valor de 30% do seu salário')
print('-//-'*10)
