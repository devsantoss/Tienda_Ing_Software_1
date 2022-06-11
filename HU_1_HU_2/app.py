# app.py
from flask import Flask, session, render_template, request, redirect, url_for
#import psycopg2
#import psycopg2.extras
import sqlite3

app = Flask(__name__)

app.secret_key = "cairocoders"

#Creacion db
connection_object = sqlite3.connect("db/tienda_database.db")
#Cursor de conexion
cursor_object = connection_object.cursor()

#DB_HOST = "localhost"
#DB_NAME = "sampledb"
#DB_USER = "postgres"
#DB_PASS = "8820"

#conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)


@app.route('/carrito')
def products():
    
    #cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    cursor_object.execute("SELECT * FROM Articulos")
    rows = cursor_object.fetchall()
    return render_template('products.html', products=rows)


@app.route('/carrito/add', methods=['POST'])
def add_product_to_cart():
    _quantity = int(request.form['quantity'])
    _id_articulo = request.form['id_articulo']
    # validate the received values
    if _quantity and _id_articulo and request.method == 'POST':

        #cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        cursor_object.execute('SELECT * FROM Articulos WHERE id_articulo = %s', (_id_articulo,))
        row = cursor_object.fetchone()

        itemArray = {
            row['id_articulo']: {'name': row['name'], 'id_articulo': row['id_articulo'], 'quantity': _quantity, 'price': row['price'],
                          'descuento': row['descuento'], 'image': row['image'],
                          'total_price': _quantity * (row['price']-row['descuento'])}}

        all_total_price = 0
        all_total_quantity = 0

        session.modified = True
        if 'cart_item' in session:
            if row['id_articulo'] in session['cart_item']:
                for key, value in session['cart_item'].items():
                    if row['id_articulo'] == key:
                        old_quantity = session['cart_item'][key]['quantity']
                        total_quantity = old_quantity + _quantity
                        session['cart_item'][key]['quantity'] = total_quantity
                        session['cart_item'][key]['total_price'] = total_quantity * (row['price'] - row['discount'])
            else:
                session['cart_item'] = array_merge(session['cart_item'], itemArray)

            for key, value in session['cart_item'].items():
                individual_quantity = int(session['cart_item'][key]['quantity'])
                individual_price = float(session['cart_item'][key]['total_price'])
                all_total_quantity = all_total_quantity + individual_quantity
                all_total_price = all_total_price + individual_price
        else:
            session['cart_item'] = itemArray
            all_total_quantity = all_total_quantity + _quantity
            all_total_price = all_total_price + _quantity * ( row['price'] - row['descuento'])

        session['all_total_quantity'] = all_total_quantity
        session['all_total_price'] = all_total_price

        return redirect(url_for('products'))
    else:
        return 'Error mientras adicionaba item al carrito'


@app.route('/carrito/empty')
def empty_cart():
    try:
        session.clear()
        return redirect(url_for('.products'))
    except Exception as e:
        print(e)


@app.route('/carrito/delete/<string:code>')
def delete_product(id_articulo):
    try:
        all_total_price = 0
        all_total_quantity = 0
        session.modified = True

        for item in session['cart_item'].items():
            if item[0] == id_articulo:
                session['cart_item'].pop(item[0], None)
                if 'cart_item' in session:
                    for key, value in session['cart_item'].items():
                        individual_quantity = int(session['cart_item'][key]['quantity'])
                        individual_price = float(session['cart_item'][key]['total_price'])
                        all_total_quantity = all_total_quantity + individual_quantity
                        all_total_price = all_total_price + individual_price
                break

        if all_total_quantity == 0:
            session.clear()
        else:
            session['all_total_quantity'] = all_total_quantity
            session['all_total_price'] = all_total_price

        return redirect(url_for('.products'))
    except Exception as e:
        print(e)


def array_merge(first_array, second_array):
    if isinstance(first_array, list) and isinstance(second_array, list):
        return first_array + second_array
    elif isinstance(first_array, dict) and isinstance(second_array, dict):
        return dict(list(first_array.items()) + list(second_array.items()))
    elif isinstance(first_array, set) and isinstance(second_array, set):
        return first_array.union(second_array)
    return False


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
