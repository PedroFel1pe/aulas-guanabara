somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = ''
contadorMulher = 0
for c in range(1,5):
    print(f'-//- {c}° pessoa -//-')
    nome = str(input('nome: ')).lower().strip()
    idade = int(input('idade: '))
    sexo: str = str(input('sexo (m/f): ')).lower().strip()
    somaIdade += idade
    # in signífica que tanto o M ou m estarão corretos
    if c == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    elif sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    elif sexo in 'Ff' and idade < 20:
        contadorMulher += 1
mediaIdade = somaIdade / 4
print(f'a média de idade entre os quatro é de {mediaIdade}')
print(f'o {nomeVelho} é o homem mais velho com {maiorIdadeHomem} anos de idade')
print(f'tem {contadorMulher} mulher com menos de 20 anos de idade')
