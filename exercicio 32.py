a = int(input('em que ano voçê nasceu?'))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('voçê nasceu em um ano bissexto')
else:
    print('voçê não faz parte de quem nasceu em um ano bissexto')
