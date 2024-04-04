print("Programa para calcular a média")

print("Por favor, digite a primeira nota:")
n = float(input())
lista.append(n)

print("Por favor, digite a segunda nota:")
n = float(input())
lista.append(n)

print("Por favor, digite a terceira nota:")
n = float(input())
lista.append(n)

media = lista[0] + lista[1] + lista[2] / 3.0
print("Sua média final é:", media)
