print("Programa tabuada")

print("Por favor digite um numero para eu calcular")
numero = int(input())

for i in range(1, 11, 1):
    res = numero * i
    print(f"{numero} X {i:>2} = {res:>2}")
    i = i + 1