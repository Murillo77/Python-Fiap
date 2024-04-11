d1 = {"nome": "Maria", "telefone": "(11) 1234-5678"}
d2 = {"nome": "João", "telefone": "(11) 1334-5558"}

lista = []
lista.append(d1)
lista.append(d2)

d = lista[1]
print("Nome: ", d['nome'] )
print("Telefone: ", d['telefone'] )