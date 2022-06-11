# UpdatePedido.py
from flask import Flask, session, render_template, request, redirect, url_for
#import psycopg2
#import psycopg2.extras
import sqlite3

# initializations
app = Flask(__name__)

app.secret_key = "cairocoders"

#Creacion db
connection_object = sqlite3.connect("db/tienda_database.db")
#Cursor de conexion
cursor_object = connection_object.cursor()
# Mysql Connection
#DB_HOST = "localhost"
#DB_NAME = "sampledb"
#DB_USER = "postgres"
#DB_PASS = "8820"

#conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)


@app.route('/update/<id>', methods=['POST'])
def update_pedido(id):
    if request.method == 'POST':
        estado = request.form['estado']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE Pedido
            SET estado = %s
            WHERE id_pedido = %s
        """, (estado, id))
        flash('Pedido Actualizado Correctamente')
        mysql.connection.commit()
        return redirect(url_for('.Index'))

# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)
