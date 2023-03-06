"""Entidades del dominio de ordenes

"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import List

from entregas.modulos.ordenes.dominio.eventos import OrdenEntregada
from entregas.seedwork.dominio.entidades import AgregacionRaiz, Entidad


@dataclass
class OrdenItems(Entidad):
    guid: str = None
    fecha_entrega: str = None
    direccion_entrega: str = None
    persona_recibe: str = None
    mecanismo_entrega: str = None


@dataclass
class Orden(AgregacionRaiz):
    guid: str = None
    fecha_creacion: str = None
    items: List[OrdenItems] = None

    def entregar_orden(self, orden: Orden):
        self.guid = orden.guid
        self.fecha_creacion = orden.fecha_creacion
        self.items = orden.items

        self.agregar_evento(OrdenEntregada(
            fecha_creacion=self.fecha_creacion,
            guid=self.guid,
            items=self.items
        ))