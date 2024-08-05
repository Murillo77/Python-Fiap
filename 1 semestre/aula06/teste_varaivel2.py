a = 79 

# como pegar este valor da variavel (a)
# como sendo octal

a_em_octal = oct(a)
print("A em octal:", a_em_octal)

# Bases numericas
# 

n1 = 8170990732
numero_em_binario = bin(n1)
numero_em_octal = oct(n1)
numero_em_hexadecimal = hex(n1)
print("Numero hexadecimal:", numero_em_hexadecimal)
print("Numero octal:", numero_em_octal )
print("N1:", n1 )
print("Numero binario: ", numero_em_binario)

n1          # 8170990732
str(n1)      # "8170990732"
print("Habitantes da terra são:" + str(n1))
print("Habitantes da terra são:", n1)

f = 971.2232434
i = int(f)
s = str(i)
print("Numero float:", f)
print("Numero inteiro:", i)
print("Numero inteiro:" + s)
