from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/tienda_database.db'
app.config['SECRET_KEY'] = "123"
db = SQLAlchemy(app)

class Pedido(db.Model):
    id  = db.Column("id_pedido", db.Integer, primary_key=True)
    cliente = db.Column("cliente",db.Integer)
    usuarioAtiende = db.Column("usuario_atiende",db.Integer)
    estado = db.Column("estado",db.Integer)
    tipoPago = db.Column("tipo_pago",db.Integer)

    def __init__(self, datos):
        self.cliente = datos["cliente"]
        self.usuarioAtiende = datos["usuarioAtiende"]
        self.estado = datos["estado"]
        self.tipoPago = datos["tipoPago"]

@app.route('/pedidos/cambiarestado/<int:id>', methods=["PUT"])
def cambiarEstadoPedido(id):
    pedido = Pedido.query.filter_by(id=id).first()
    if pedido:
        pedido["estado"] = pedido["estado"] + 1
        try:
            db.session.commit()
            return "Estado cambiado correctamente", 200
        except Exception as error: 
            print(str(error.orig) + "for parameters" + str(error.params))
            return "No puede cambiar más el estado", 405
    else:
        return "Not found Id", 404
    db.session.update