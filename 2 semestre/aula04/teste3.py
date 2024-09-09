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

ddl_tabela_pets = """
    CREATE TABLE tabela_pets(
        id NUMBER(10),
        nome VARCHAR2(60),
        raça VARCHAR2(60),
        idade NUMBER(5),
        CONSTRAINT pets_pk PRIMARY KEY (id)
    )

"""

cursor = con.cursor()
cursor.execute(ddl_tabela_pets)
con.commit()

print("Tabela foi criada")

print("Database version:", con.version)

print("Usuario: ", user)