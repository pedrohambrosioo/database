import mysql.connector
from mysql.connector import Error
from flask import Flask, render_template, redirect
from flask import request


class Pessoa:
    def __init__(self, user, senha, ID):
        self.user = user
        self.senha = senha
        self.id = ID
        valor = ""
    
                 
    def cadastra(self):                                 
        try: 
            con = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "admin",
            database = "dbprojeto")   
            consulta = f"""SELECT * FROM cadastro WHERE USER = '{self.user}';"""
            cursor = con.cursor()
            cursor.execute(consulta)
            linhas = cursor.fetchall()    
            
            if(cursor.rowcount >= 1):  
                setattr(Pessoa, "valor", "nao deu certo")
                
                #colocar variavel de sinal de verificacao                 
              
            else:               
                inf = "\"" + self.user + "\"" + ",\"" + self.senha + "\")" 
                declaracao = """INSERT INTO cadastro 
                    (user,senha)
                    VALUES ("""
                sql = declaracao + inf                                  
                cursor = con.cursor()
                cursor.execute(sql)
                con.commit()
                cursor.close() 
                setattr(Pessoa, "valor", "deu certo")
                

        except Error as erro:
            print(erro)                   
        finally:
            if (con.is_connected()):
                cursor.close()
                con.close()               
    
    def login(self):
        try:
            con = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "admin",
                database = "dbprojeto")   
            
            consulta = f"""SELECT * FROM cadastro WHERE USER = '{self.user}';"""
            cursor = con.cursor()
            cursor.execute(consulta)
            linhas = cursor.fetchall()    
                
            if(cursor.rowcount >= 1): 
                if(self.senha == consulta[2] and self.user == consulta[1]):
                    acesso = True
                    #consegiu se logar
                    #retorna a pagina de acesso dele 
                else:
                    acesso = False 

        except Error as erro:
                print(erro)
                    
        finally:
            if (con.is_connected()):
                cursor.close()
                con.close()



    def atualizar(self):    
        con = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "admin",
            database = "dbprojeto")    
        consulta = f"""SELECT * FROM cadastro WHERE USER = '{self.user}';"""
        cursor = con.cursor()
        cursor.execute(consulta)
        linhas = cursor.fetchall()

        if(cursor.rowcount >= 1):  
                self.valor = False
        
        else:
            atualizacao = f"""UPDATE cadastro SET USER ='{self.user}', SENHA = '{self.senha}' WHERE ID = "{self.id}"  """   
            
            try: 
                con = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "admin",
                database = "dbprojeto")                                         
                cursor = con.cursor()
                cursor.execute(atualizacao)
                con.commit()
                cursor.close()
                
            except Error as erro:
                print(erro)
                    
            finally:
                if (con.is_connected()):
                    cursor.close()
                    con.close()

    def deletar(self):
        delete = f"""DELETE FROM cadastro WHERE ID = "{self.id}"; """   
        
        try: 
            con = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "admin",
            database = "dbprojeto")                                         
            cursor = con.cursor()
            cursor.execute(delete)
            con.commit()
            cursor.close()
            
        except Error as erro:
            print(erro)
                
        finally:
            if (con.is_connected()):
                cursor.close()
                con.close()
    
    def retorno(self):
        return self.msg

def criar():
    user = str(request.form.get("user"))
    senha = str(request.form.get("senha"))
    cadastro = Pessoa(user,senha,"")
    cadastro.cadastra()
    valor = getattr(cadastro, "msg")
    
def update():
    user = str(request.form.get("userNew"))
    senha = str(request.form.get("senhaNew"))
    Chave_de_seguranca = str(request.form.get("ID"))
    atualiza = Pessoa(user, senha, Chave_de_seguranca)
    atualiza.atualizar()

def delete():
    user = str(request.form.get("userDel"))
    senha = str(request.form.get("senhaDel"))
    Chave_de_seguranca = str(request.form.get("IDD"))
    delete = Pessoa("","",Chave_de_seguranca)
    delete.deletar()



getattr(Pessoa, "valor")


