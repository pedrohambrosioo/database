#WEB CONFIG---------------------------------
import mysql.connector
from mysql.connector import Error
from flask import Flask, render_template, redirect
from flask import request
from classes import Pessoa, criar, update, delete


app= Flask(__name__)

@app.route("/parabens")
def mensagem(): 
    return render_template("parabens.html")

@app.route("/")
def home():
    return render_template("home.html")
#-------------------CADASTRO-----------------
@app.route("/cadastro")
def homepage():
    return render_template("cad.html")
@app.route("/cadastro", methods=["POST"])
def ceste(): 
    mensagem = ""
    return render_template("cad.html", mensagem = mensagem), criar()
#-------------------------------------------
#------------------UPDATE---------------        
@app.route("/update")
def up():
    return render_template ("atualiza.html")
@app.route("/update", methods=["POST"])
def updt():
    return redirect("/update"), update()
#-------------------------------------------   
#------------------DELETE-------------------
@app.route("/delete")
def dell():
    return render_template("delete.html")
@app.route("/delete", methods=["POST"])
def deld():
    return redirect("/parabens"), delete()
#--------------------------------------------

@app.route("/error")
def er():
    return render_template("erro.html")
#---------------LOGIN---------------------------
@app.route("/login")
def lg():
    return render_template("login.html")
@app.route("/login", methods = ["POST"])
def lg1():
    return render_template("login.html")

#------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
