x = int(input('Digite a coordenada x: '))
y = int(input('Digite a coordenada y: '))

if 10 > x > 0 and 10 > y > 0:
    print('Dentro do quadrado')
elif x == 0 or x == 10 or y == 0 or y == 10:
    print('Na fronteira')
else:
    print('Fora do quadrado')