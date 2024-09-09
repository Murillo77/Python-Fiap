import requests

url = "https://tdspm-ce89a-default-rtdb.firebaseio.com/contatos.json"

contato = { "nome": "Yuri Alberto",
            "telefone": "(11) 2222222",
          }

response = requests.post(url, json=contato)

print(response)