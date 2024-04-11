print("Digite a quantidade de galhos da árvore:")
galhos = int(input())

for a in range(0, galhos + 1):
    qtd_espaco = galhos - a
    print(" " * qtd_espaco, end="")
    asterisco = (a * 2) - 1
    print("*" * asterisco)