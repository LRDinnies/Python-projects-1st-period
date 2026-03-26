ingresso = input('Deseja comprar o ingresso? ')
if ingresso == 'sim':
    idade = int(input('Qual sua idade: '))
    if idade >= 18:
        print('Pode entrar')
    else:
        print('Você não possui idade necessaria')
else:
    print('Você não possui ingresso')