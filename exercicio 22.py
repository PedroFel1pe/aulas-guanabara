frase = str(input('qual o seu nome?')).strip()
#.strip é para desconsiderar os espaços antes e depois da frase
print(len(frase) - frase.count(' '))
print(frase.upper())
print(frase.lower())
dividir = frase.split()
print(len(dividir[0]))
# count identifica os espaços no meio das frases
