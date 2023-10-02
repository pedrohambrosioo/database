import mysql.connector
from mysql.connector import Error

user = input("user: ")
senha = input("senha: ")
inf = "\"" + user + "\"" + ",\"" + senha + "\")" 
declaracao = """INSERT INTO cadastro 
(user,senha)
VALUES ("""
sql = declaracao + inf
    
try: 
    con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "admin",
    database = "dbprojeto")   
                    
    inserir_dados = sql          
    cursor = con.cursor()
    cursor.execute(inserir_dados)
    con.commit()
    print(cursor.rowcount, "registros inseridos na tabela")
    cursor.close()
        
except Error as erro:
    print("Falha  ao inserir os dados no mysql: {}".format(erro))
        
finally:
    if (con.is_connected()):
        cursor.close()
        con.close()
        print("conexao mysql finalizada")
