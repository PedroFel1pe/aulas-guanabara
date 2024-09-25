print('\033[;5;36m --//--\033[;;m' * 10)
import random
print('Que tal uma partida de jokenpô, para ver como esta sua sorte')
escolha = str(input('''escolha uma das alternativas 
pedra
papel 
tesoura
então o que sera?'''))
stone = 'pedra'
paper = 'papel'
scissors = 'tesoura'
list = [stone, paper, scissors]
result = random.choice(list)
print(F'EU ESCOLHO {result}')
if escolha == result:
    print(f'esta foi empate ambos escolhemos {escolha}')
elif escolha == 'pedra' and result == 'papel':
    print('\033[;5;31mVoçê perdeu, mas não desanime')
elif escolha == 'papel' and result == 'tesoura':
    print('\033[;5;31mVoçê perdeu, mas não desanime')
elif escolha == 'tesoura' and result == 'pedra':
    print('\033[;5;31m Voçê perdeu, mas não desanime')
else:
    print('\033[;5;33m Parabens voçê ganhou!!!!!')
print('\033[;5;36m --//--' * 10)
