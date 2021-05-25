import psycopg2

h=input("Introduce la ip del servidor: ")
d=input("Introduce el nommbre de la base de datos: ")
u=input("Introduce el usuario: ")
p=input("Introduce contraseña: ")

conexion=psycopg2.connect(host=h,database=d,user=u,password=p)
if conexion == "":
    print("No se encuentra ningún servidor")
else:
    cur = conexion.cursor()
    cur.execute( "SELECT nombre, apellidos FROM medicos" )
    for nombre, apellidos in cur.fetchall() :
        print (nombre,apellidos)
conexion.close()

