track = input('Você chega a uma bifurcação, qual caminho deseja seguir? Direita ou esquerda? ')
if track == 'direita':
    mountain = input('Você se depara com uma montanha, deseja escalar? ')
    if mountain == 'sim':
        print('Você encontrou um tesouro')
    else:
        print('Você voltou à bifurcação')
elif track == 'esquerda':
    river = input('Você chega a um rio, deseja atravessar? ')
    if river == 'sim':
        print('Você chega ao outro lado e encontra uma vila onde pode passar a noite')
    else:
        print('Você voltou a bifurcação')
else:
    print('Você permanece parado pensando em sua decisão')
