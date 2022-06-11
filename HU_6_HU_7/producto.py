from flask import Flask, url_for, redirect
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/tienda_database.db'
app.config['SECRET_KEY'] = "123"

db = SQLAlchemy(app)

class producto(db.Model):
    id  = db.Column("product_id", db.Integer, primary_key=True)
    producto_nombre = db.Column(db.String(100))
    producto_valor = db.Column(db.Integer)
    producto_cantidad = db.Column(db.Integer)

    def __init__(self, datos):
        self.producto_nombre = datos["nombre"]
        self.producto_cantidad = datos["cantidad"]
        self.producto_valor = datos["valor"]

@app.route("/") # listar productos
def principal():
    data = producto.query.all()
    diccionario_productos = {}
    for d in data:
        p = {"id": d.id,
             "nombre": d.producto_nombre,
             "cantidad": d.producto_cantidad,
             "valor": d.producto_valor
            }
        diccionario_productos[d.id] = p
    return diccionario_productos

@app.route("/eliminar/<int:id>")# eliminar productos
def eliminar(id):
    p = producto.query.filter_by(id=id).first()
    db.session.delete(p)
    db.session.commit()
    return redirect(url_for('principal'))
