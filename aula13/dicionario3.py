lista = []
for i in range(0,3):
    print("Digite o nome: ")
    nome = input()
    print("Digite o telefone: ")
    telefone = input()
    print("Digite a idade: ")
    idade = int(input())

    d = {   "nome": nome,
            "telefone": telefone,
            "idade": idade}
    lista.append(d)

for i in range(0,3):
    print("Nome: ", d['nome'])
    print("Telefone: ", d['telefone'])
    print("Idade: ", d['idade'])
    print()
