def pedir_numero(texto = "Digite um numero: "):
    """""
    Função utilizada para  pedir numero inteiro e verificar se é valido!

    """""
    valido = False
    while not valido:
        print(texto)
        digitado = input()
        try:
             n = int(digitado)
             valido = True

        except:
            print(f"Erro! Por favor, digite um número inteiro.")
        print("Numero digitado: ", n)
    return n

print("Inicio programa ")
n1 = pedir_numero("Digite o 1º numero: ")
n2 = pedir_numero("Digite o 2º numero: ")
soma = n1 + n2
print(f"A soma dos dois numero é:", soma)
print("fim programa")


