import sqlite3

#Creacion db
connection_object = sqlite3.connect("../.db/tienda_database.db")
#Cursor de conexion
cursor_object = connection_object.cursor()
#lectura del sql
sql_file = open("dbScript.sql")
sql_as_string = sql_file.read()
#Ejecucion del script
cursor_object.executescript(sql_as_string)