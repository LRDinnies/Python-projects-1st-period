verify = False
while verify == False:
    nota = float(input('Digite sua nota: '))
    if nota >= 0 and nota <= 10:
        print('Sua nota é valida.')
        verify = True
    else:
        print('Nota invalida.')