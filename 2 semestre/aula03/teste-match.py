print ( """
    (1) Cadastrar-se
    (2) Mostrar
    (3) Remover
    (4) Atualizar
    (X) Sair
""")

opcao = int(input("ESCOLHA UMA OPÇÃO SEU ARROMBADINHO: "))

match opcao:
    case 1:
        input("Digite seu email: ")
        input("Digite sua senha: ")
    case 2:
        print("aa")
    case 3:
        print("remover")