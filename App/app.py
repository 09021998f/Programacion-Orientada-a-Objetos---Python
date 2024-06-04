from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.config.from_pyfile('config.py')
from models import *


@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/sucursales')
def mostrar_sucursales():
    return render_template('sucursales.html', sucursales = Sucursal.query.all())

@app.route('/transportes')
def mostrar_transportes():
    transportes = Transporte.query.all()
    return render_template('transportes.html', transportes=Transporte.query.all())

@app.route('/repartidores')
def mostrar_repartidores():
    repartidores = Repartidor.query.all()
    return render_template('repartidores.html', repartidores=Repartidor.query.all())

@app.route('/paquetes')
def mostrar_paquetes():
    paquetes = Paquete.query.all()
    return render_template('paquetes.html', paquetes=Paquete.query.all())

'''Aqui empieza la applicacion a entregar'''

@app.route('/despachante', methods = ['GET', 'POST'])
def home_despachante():
    
    if request.method == 'POST':
        print('hola')
        if not request.form['sucursal']:
            return render_template('home_despachante.html', sucursales = Sucursal.query.all())
        else:
            id = request.form['sucursal']
            print(id)
            return render_template('sucursal.html', sucursales = Sucursal.query.get(id))            
    else:
        return render_template('home_despachante.html', sucursales = Sucursal.query.all())


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)