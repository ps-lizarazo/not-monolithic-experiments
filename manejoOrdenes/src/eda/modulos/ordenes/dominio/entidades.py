"""Entidades del dominio de Ordenes

En este archivo usted encontrará las entidades del dominio de Ordenes

"""

from __future__ import annotations
from dataclasses import dataclass, field

import eda.modulos.ordenes.dominio.objetos_valor as ov
from eda.seedwork.dominio.entidades import Locacion, AgregacionRaiz, Entidad

@dataclass
class CentroDeDistribucion(AgregacionRaiz):
    items: list[ov.Item] = field(default_factory=list[ov.Item])   

@dataclass
class Orden(AgregacionRaiz):
    items: list[ov.Item] = field(default_factory=list[ov.Item])
