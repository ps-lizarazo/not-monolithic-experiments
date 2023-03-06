import os
from flask import Flask, render_template, request, url_for, redirect, jsonify

my_app = None
# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

def importar_modelos_alchemy():
  import ordenes.modulos.pedidos.infraestructura.dto

def create_app(configuracion=None):
  # Init la aplicacion de Flask
  app = Flask(__name__, instance_relative_config=True)

  global my_app
  my_app = app

  # Configuracion de BD
  app.config['SQLALCHEMY_DATABASE_URI'] =\
          'sqlite:///' + os.path.join(basedir, 'database.db')
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

  # Inicializa la DB
  from ordenes.config.db import init_db
  init_db(app)

  from ordenes.config.db import db

  importar_modelos_alchemy()

  with app.app_context():
        db.create_all()

  # Importa Blueprints
  from . import pedidos


  app.register_blueprint(pedidos.bp)

  @app.route("/health")
  def health():
    return {"status": "up"}

  return app