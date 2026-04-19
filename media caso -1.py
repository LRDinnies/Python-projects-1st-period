soma_total = 0
quantidade_numeros = 0

numero = int(input("Digite um número (-1 para encerrar): "))

while numero != -1:
    soma_total = soma_total + numero
    quantidade_numeros = quantidade_numeros + 1

    numero = int(input("Digite um número (-1 para encerrar): "))

if quantidade_numeros > 0:
    media = soma_total / quantidade_numeros
    print("Média:", media)
else:
    print("Nenhum número foi digitado.")