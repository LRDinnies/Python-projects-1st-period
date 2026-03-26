#Exercicio input/output
#Input de dados:
nome = input("Digite seu nome: ")
cpf = input("Digite seu CPF: ")
telefone = input("Digite seu telefone: ")
ano = int(input("Digite seu ano de nascimento: "))
print()

#Resultados dos dados inseridos:
print("Seu nome é: ", nome)
print("Seu cpf é: ", cpf)
print("Seu telefone é: ", telefone)
print("Você nasceu em: ", ano)
print()

print("Resultado final de dados:", nome, cpf, telefone, ano)
print()

#Verificação de maioridade:
if 2026-ano >= 18:
    print("Você é maior de idade")
else: print("Você é menor de idade")
print()

#Cálculo de IMC:
peso = float(input("Digite seu peso(Kg): "))
altura = float(input("Digite sua altura(m): "))
imc = peso / (altura ** 2)
print("Seu IMC é igual a: ", imc)


if imc << 18.5:
    print("Você possui bixo peso")
if imc >= 18.5 and imc <= 24.99:
    print("Você possui peso adquado")
if imc >= 25.0 and imc <= 29.99:
    print("Você possui sobrepeso")
if imc >= 30.0
    print("Você possui obesidade")