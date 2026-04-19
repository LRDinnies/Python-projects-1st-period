while True:
    print("--- Calculadora ---")
    print("1: soma")
    print("2: subtração")
    print("3: multiplicação")
    print("4: divisão")
    print("0: sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 0:
        print("Encerrando...")
        break

    elif opcao >= 1 and opcao <= 4:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if opcao == 1:
            print("Resultado:", num1 + num2)

        elif opcao == 2:
            print("Resultado:", num1 - num2)

        elif opcao == 3:
            print("Resultado:", num1 * num2)

        elif opcao == 4:
            if num2 == 0:
                print("Erro: divisão por zero!")
            else:
                print("Resultado:", num1 / num2)

    else:
        print("Opção inválida!")