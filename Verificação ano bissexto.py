ano = int(input('Insira o ano que deseja verificar se é bissexto: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Sim, esse ano é bissexto')
else:
    print('Não, esse ano não é bissexto')