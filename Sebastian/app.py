from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/tienda_database.db'
app.config['SECRET_KEY'] = "123"
db = SQLAlchemy(app)

@app.route('/pedidos', methods=["PUT"])
def modificarPedido():
    return f'Holi'