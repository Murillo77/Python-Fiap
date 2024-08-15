class Pessoa:
    nome = ""
    sobrenome = ""

    def imprimir(self):
        print(f"Nome: {self.nome} \t\tSobrenome: {self.sobrenome} ")

p1 = Pessoa()
p1.nome = "Joao"
p1.sobrenome = "Silva"
p1.imprimir()


p2 = Pessoa()
p2.nome = "Joana"
p2.sobrenome = "Silva"
p2.imprimir()