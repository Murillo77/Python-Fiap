import requests
import json

url = "https://tdspm-ce89a-default-rtdb.firebaseio.com/contatos.json"

response = requests.get(url)

texto = response.text

print("Response: ", response)
print("Corpo: ", response.text)

contatos = json.loads(texto)

print("Chaves dos contatos: ")
for chave in contatos.keys():
    print(chave)

for contato in contatos.values():
    print(f"Nome: {contato['nome']}\tTelefone: {contato['email']}")