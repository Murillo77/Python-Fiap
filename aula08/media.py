print("Programa para calcular a media final de alunos(as)")

executar = True

while executar:
    print("Por Favor digite seu nome")
    nome = input()

    print("Por favor informe a nota 1")
    nota1 = float(input())

    print("Por favor informe a nota 2")
    nota2 = float(input())

    print("Por favor informe a nota 3")
    nota3 = float(input())

    media = (nota1 + nota2 + nota3) / 3
    print("Nome         Nota 1   Nota 2    Nota 3    Média")
    print(f"{nome:<12}{nota1:<9.1f}{nota2:<9.1f}{nota3:<9.1f}{media:<5.1f}")

    print("Deseja calcular a media de outro estudante (S/N)?")
    escolha = input()
    if escolha == 'N':
        executar = False
    print("Fim do programa!")





