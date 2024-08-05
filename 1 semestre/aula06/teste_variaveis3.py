s = "Ola Mundo!!!"
print("Texto:" + s)

s_minusculo = s.lower()
print("Texto Minusculo:", s_minusculo)
s_maiusculo = s.upper()
print("Texto Maiusculo:", s_maiusculo)

tamanho = len(s)
print("Tamnaho da string:", tamanho)
print("Tamanho da string:" + str(tamanho))

texto = "A fiap é uma faculdade bem legal"
tam = len(texto)
print("Tamanho:", tam)
letra = texto[17]
print("Letra na posição 17 é:" + letra)
letra = texto[20]
print("Letra na posição 20 é:" + letra)

pos = texto.find("legal")
print("O texto possui a palavra legal na posção:", pos)

pos = texto.find("fiap")
print("O texto possui a palavra fiap na posição:", pos)

pos = texto.find("manha")
print("O texto possui a palavra manha na posição:", pos)

pos = texto.find("m")
print("O texto possui a letra m na posição:", pos)

pos = texto.find("m", 11)
print("O texto possui outra letra m na posição:", pos)

pos = texto.find("m", 11)
print("O texto possui outra letra m na posição:", pos)
