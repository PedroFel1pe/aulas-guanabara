print('verificando se a frase é um palindromo(se ler de tras pra frente continua a mesma frase)')
frase = str(input('digite a frase:')).strip().lower()
fraseSemEspaco = frase.split()
junto = ''.join(fraseSemEspaco)
invertido = ''
for letra in range(len(junto)-1, -1, -1):
    invertido += junto[letra]
if junto == invertido:
    print(f'esta frase é um palindromo {invertido}')
else:
    print(f'esta frase não é um palindromo {invertido}')