"""Objetos valor del dominio de ordenes

En este archivo usted encontrará los objetos valor del dominio de ordenes

"""

from __future__ import annotations

from dataclasses import dataclass, field
from eda.seedwork.dominio.objetos_valor import ObjetoValor
from datetime import datetime


@dataclass(frozen=True)
class NombreCentroDistribucion():
    nombre: str

@dataclass(frozen=True)
class DireccionRecogida():
	pais: str = field(default_factory=str)
	ciudad: str = field(default_factory=str)
	direccion: str = field(default_factory=str)
	codigo_postal: str = field(default_factory=str)
	telefono_responsable: str = field(default_factory=str)
	nombre_responsable: str = field(default_factory=str)

@dataclass(frozen=True)
class DireccionEntrega():
	pais: str = field(default_factory=str)
	ciudad: str = field(default_factory=str)
	direccion: str = field(default_factory=str)
	codigo_postal: str = field(default_factory=str)
	telefono_responsable: str = field(default_factory=str)
	nombre_responsable: str = field(default_factory=str)


@dataclass(frozen=True)
class Item(ObjetoValor):
	nombre: str = field(default_factory=str)
	cantidad: int = field(default_factory=int)
   

   
