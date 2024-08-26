import os
import oracledb
 
user = os.environ.get("PYTHON_ORACLE_USER")
senha = os.environ.get("PYTHON_ORACLE_PASS")
db = "oracle.fiap.com.br:1521/orcl"
 
con = oracledb.connect(
    user=user,
    password=senha,
    dsn=db
)
 
print(con.version)
 
sql = """
    INSERT INTO times_futebol (id, nome, jogadores, vitorias, derrotas, empates, animo)
    VALUES (1, 'Corinthians', 26, 58, 2, 12, 100)
"""
 
cursor = con.cursor()
cursor.execute(sql)
con.commit()
print("Registro inserido com sucesso")




















ddl_pets = """
    CREATE TABLE times_futebol(
        id NUMBER(10),
        nome VARCHAR2(60),
        raça VARCHAR2(60),
        idade NUMBER(5),
        CONSTRAINT pets_pk PRIMARY KEY (id)
    )

"""

cursor = con.cursor()
cursor.execute(ddl_pets)
con.commit()

print("Tabela foi criada")