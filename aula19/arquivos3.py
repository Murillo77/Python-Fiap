arquivo1 = open("./teste.csv", "r", encoding="utf-8")
arquivo1.write("Murillo|(11)98561-9925|18\n")
arquivo1.write("Rayssa|(11)99013-9668|19\n")
arquivo1.write("BlaBlaBla|(11)99013-9668|19\n")

texto = arquivo1.readline()
print("Texto: ", texto)
arquivo1.close()