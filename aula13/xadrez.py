print("Programa para fazer um tabuleiro de xadrez")

linha1 = ""
caractere = "#"

for j in range(0,8):
    for i in range(0,5):
        linha1 += caractere
    caractere = " " if caractere == "#" else "#"
print(linha1)

caractere = " "
linha2 = ""

for j in range(0,8):
    for i in range(0,5):
        linha2 += caractere
    caractere = " " if caractere == "#" else "#"
print(linha1)
print(linha2)    


for j in range(4):
    for i in range(0,3):
        print(linha1)
    for i in range(0,3):
        print(linha2)