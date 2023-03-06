from ordenes.config.db import db

from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Table

import uuid

class Orden(db.Model):
    __tablename__ = "orden"
    id = db.Column(db.String(40), primary_key=True)
    fecha_creacion = db.Column(db.DateTime, nullable=True)
    fecha_actualizacion = db.Column(db.DateTime, nullable=True)
    items= db.relationship('Item', cascade = 'all, delete, delete-orphan')

class Item(db.Model):
    __tablename__ = "item"
    id = db.Column(db.String(40), primary_key=True)
    nombre = db.Column(db.String(100))
    cantidad = db.Column(db.Integer)
    fecha_creacion = db.Column(db.DateTime, nullable=True)
    fecha_actualizacion = db.Column(db.DateTime, nullable=True)
    pais_recogida = db.Column(db.String(60))
    ciudad_recogida = db.Column(db.String(60))
    direccion_recogida = db.Column(db.String(60))
    codigo_postal_recogida = db.Column(db.String(60))
    telefono_responsable_recogida = db.Column(db.String(60))
    nombre_responsable_recogida = db.Column(db.String(60))
    pais_entrega = db.Column(db.String(60))
    ciudad_entrega = db.Column(db.String(60))
    direccion_entrega = db.Column(db.String(60))
    codigo_postal_entrega = db.Column(db.String(60))
    telefono_responsable_entrega = db.Column(db.String(60))
    nombre_responsable_entrega = db.Column(db.String(60))
    orden = db.Column(db.String(40),db.ForeignKey('orden.id'))