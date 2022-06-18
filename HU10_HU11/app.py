from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/tienda_database.db'
app.config['SECRET_KEY'] = "123"
db = SQLAlchemy(app)

#app.secret_key = 

@app.route("/descuentos")
def descuentos():
    return 'Hola mundo'


if __name__ == "__main__":
    app.run(port=3001, debug=True, host='0.0.0.0')
