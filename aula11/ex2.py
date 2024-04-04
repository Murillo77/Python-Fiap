print("Programa")

lista = []

for i in range(10):
     print(f"Por favor, digite a medida da planta na {i + 1}º semana:")
     altura = float(input())
     lista.append(altura)

print("Lista:", lista)

soma = 0 
for i in range(3):
   numero = lista[i]
   soma = soma + numero
   print("Numero:", numero, "\tSoma:", soma)

media = soma / 3
print("A média é:", media)