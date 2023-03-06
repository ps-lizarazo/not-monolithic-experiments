""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de ordenes

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de ordenes

"""

from ordenes.config.db import db
from ordenes.modulos.pedidos.dominio.repositorios import RepositorioItems,RepositorioOrdenes
#from ordenes.modulos.pedidos.dominio.objetos_valor import NombreAero, Odo, Leg, Segmento, Itinerario, CodigoIATA
from ordenes.modulos.pedidos.dominio.entidades import Orden
from ordenes.modulos.pedidos.dominio.fabricas import FabricaPedido
from .dto import Orden as OrdenDTO
from .mapeadores import MapeadorOrden
from uuid import UUID



class RepositorioOrdenesSQLite(RepositorioOrdenes):

    def __init__(self):
        self._fabrica_pedido: FabricaPedido = FabricaPedido()

    @property
    def fabrica_pedido(self):
        return self._fabrica_pedido

    def obtener_por_id(self, id: UUID) -> Orden:
        orden_dto = db.session.query(OrdenDTO).filter_by(id=str(id)).one()
        return self.fabrica_pedido.crear_objeto(orden_dto, MapeadorOrden())

    def obtener_todos(self) -> list[Orden]:
        # TODO
        raise NotImplementedError

    def agregar(self, orden: Orden):
        orden_dto = self.fabrica_pedido.crear_objeto(orden, MapeadorOrden())
        db.session.add(orden_dto)
        db.session.commit()

    def actualizar(self, orden: Orden):
        # TODO
        raise NotImplementedError

    def eliminar(self, orden_id: UUID):
        # TODO
        raise NotImplementedError