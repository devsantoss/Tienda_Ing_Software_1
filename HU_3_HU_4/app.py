from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/tienda_database.db'
app.config['SECRET_KEY'] = "123"
db = SQLAlchemy(app)

CODIGO_ANTES_DESPACHO = 2

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

@app.route('/pedidos/<int:id>/cambiarestado', methods=["PUT"])
def cambiarEstadoPedido(id):
    pedido = Pedido.query.filter_by(id=id).first()
    if pedido:
        pedido["estado"] = pedido["estado"] + 1
        try:
            db.session.commit()
            db.session.update()
            return "Estado cambiado correctamente", 200
        except Exception as error: 
            print(str(error.orig) + "for parameters" + str(error.params))
            return "No puede cambiar más el estado", 405            
    else:        
        return "Not found Id", 404
        
@app.route('/pedidos/<int:id>/asignardomiciliario', methods=["PUT"])
def asignarDomiciliario(id):
    pedido = Pedido.query.filter_by(id=id).first()
    if pedido:
        if(pedido.estado == CODIGO_ANTES_DESPACHO):
            pedido["usuarioAtiende"] = request.data.usuarioAtiende
            try:
                db.session.commit()
                db.session.update()
                return "Domiciliario asignado correctamente", 200
            except Exception as error: 
                print(str(error.orig) + "for parameters" + str(error.params))
                return "No puede cambiar más el estado", 405