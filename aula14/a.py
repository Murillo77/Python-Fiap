d1 = {
    "alunos": 40,
    "professor": "Antonio",
    "computadores": 43,
    "cadeiras": 43,
    "monitores": 43,
    "perifericos":{
                    "computadores": 43,
                    "monitores": 43
                   }
}

d1["sala_aula"] = 201

if "sala_aula" in d1:
    print("Existe a chave 'sala_aula' no dicionario")
else:
     print("Não existe a chave 'sala_aula' no dicionario")

#chaves = list(d1.keys())
#tamanho = len(chaves)
#for i in range(tamanho):
    # chave = d1.keys[i]
    # print(chaves)

for chave in d1.keys():
     print(chave, "==>", d1[chave])
     
