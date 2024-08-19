lista = ['bom', 'dia', 'joao', 'Maria', 'Jose']

match lista:
    case [saudacao, periodo, nomes ]:
        for nome in nomes:
            print(saudacao, periodo, nome)