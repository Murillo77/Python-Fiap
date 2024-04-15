lista = []
print("Digite o nome da fruta: " )
nome = input()
print("Digite a cor da fruta: " )
cor = input()
print("Digite o preço da fruta: " )
preco = float(input())

d1 = {
    "Nome": nome,
    "Cor": cor,
    "Preço": preco,
}

lista.append(d1)
print(d1)