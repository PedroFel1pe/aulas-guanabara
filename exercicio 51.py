# ler um número e a sua PA(ordem que ele vai ocorre) e digita 10 valores dessa sequência
num = int(input('informe o numero inicial = '))
razao = int(input('agora a progressão aritmética que ocorrera = '))
decimo = num + (11 - 1) * razao
for c in range(num, decimo, razao):
    print(c, end=', ')
