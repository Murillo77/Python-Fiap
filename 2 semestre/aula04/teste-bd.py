import os
import oracledb

user = os.environ.get("PYTHON_ORACLE_USER")
senha = os.environ.get("PYTHON_ORACLE_PASS")
db_path="oracle.fiap.com.br:1521/orcl"
con = oracledb.connect(
    user=user,
    password=senha,
    dsn=db_path
)

ddl_times_futebol = """
    CREATE TABLE times_futebol(
        id NUMBER(10),
        nome VARCHAR2(60),
        jogadores NUMBER(5),
        vitorias NUMBER(5),
        derrotas NUMBER(5),
        empates NUMBER(5),
        animo NUMBER(5),
        CONSTRAINT times_futebol_pk PRIMARY KEY (id)
    )

"""



cursor = con.cursor()
cursor.execute(ddl_times_futebol)
con.commit()
print("Tabela foi criada")

print("Database version:", con.version)

print("Usuario: ", user)