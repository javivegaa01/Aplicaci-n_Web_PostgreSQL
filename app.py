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
    conexion=psycopg2.connect(host="192.168.121.187",database=d,user=u,password="usuario")
    cur = conexion.cursor()
    lista_tablas=['medicos','pacientes','horasdeconsulta','salasdeconsultas']
    lista_columnas=[]
    for a in lista_tablas:
        cur.execute("select column_name from information_schema.columns where table_name='%s';" % a)
        lista=[]
        for a in cur.fetchall():
            lista.append(str(a))
        lista_columnas.append(lista)
    lista_resultados=[]
    for a in lista_tablas:
        cur.execute("select * from %s;" % a)
        lista=[]
        for a in cur.fetchall():
            lista.append(a)
        lista_resultados.append(lista)
    return render_template("postgres.html",d=d,lista_tablas=lista_tablas,lista_columnas=lista_columnas,num=len(lista_tablas),lista_resultados=lista_resultados)

port=os.environ["PORT"]
app.run('0.0.0.0',int(port),debug=False)


