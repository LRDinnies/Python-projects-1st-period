user = input('Digite o usuário correto: ')
if user == 'admin':
    senha = int(input('Digite sua senha: '))
    if senha == 1234:
        print('Senha valida! Acesso concedido')
elif user == 'convidado':
    print('Acesso restrito concedido')
else:
    print('Acesso negado')