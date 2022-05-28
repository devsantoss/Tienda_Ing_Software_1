from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

# initializations
app = Flask(__name__)

# Mysql Connection
app.config['MYSQL_HOST'] = 'localhost' 
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flaskcrud'
mysql = MySQL(app)

# settings
app.secret_key = "mysecretkey"

# route

@app.route('/update/<id>', methods=['POST'])
def update_pedido(id):
    if request.method == 'POST':
        id_estad = request.form['id_estad']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE contacts
            SET id_estad = %s
            WHERE id = %s
        """, (id_estad, id))
        flash('Pedido Actualizado Correctamente')
        mysql.connection.commit()
        return redirect(url_for('Index'))

# starting the app
if __name__ == "__main__":
    app.run(port=3000, debug=True)
