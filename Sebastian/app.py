from flask import Flask
import sqlite3

app = Flask(__name__)

#Creacion db
connection_object = sqlite3.connect(".db/tienda_database.db")
#Cursor de conexion
cursor_object = connection_object.cursor()

@app.route('/pedidos', methods=["PUT"])
def modificarPedido():
    return f'Holi'
