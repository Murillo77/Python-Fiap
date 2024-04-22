texto = """
    public class TesteJava1 {
        public static void main(String[] args){
            System.out.println("Teste 1 feito em Java")
    }
}
"""
arquivo1 = open("./testeJava1.txt", "w", encoding="utf-8")
arquivo1.write("Você mora em itaquera\n")
arquivo1.write("Tá me tirando caralho\n")
arquivo1.write("!!!!!!!\n")
arquivo1.close()