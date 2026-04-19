contador = 0
par = 0
impar = 0
while contador < 10:
    valor = int(input("Digite um numero: "))
    if valor % 2 == 0:
        par = par + 1
        contador = contador + 1
    else:
        impar = impar + 1
        contador = contador + 1
print(f'A quantia de números pares é {par} e a de impares {impar}')