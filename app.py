import os
import psycopg2
from flask import Flask, render_template,abort,request
app = Flask(__name__)	

@app.route('/',methods=["GET"])
def inicio():
    return render_template("inicio.html")

@app.route('/formulario',methods=["GET"])
def formulario():
    return render_template("formulario.html")

@app.route('/postgres',methods=["POST"])
def postgres():
    d=request.form.get("d")
    u=request.form.get("u")
    p=request.form.get("p")
    conexion=psycopg2.connect(host="192.168.1.42",database=d,user=u,password="usuario")
    cur = conexion.cursor()
    #cur.execute( "SELECT nombre, apellidos FROM medicos" )
    cur.execute( "\l" )
    for a in cur.fetchall() :
        mostrar.append(a)
    conexion.close()
    return render_template("postgres.html",mostrar=mostrar,d=d)

#port=os.environ["PORT"]
#'0.0.0.0',int(port)
app.run(debug=True)