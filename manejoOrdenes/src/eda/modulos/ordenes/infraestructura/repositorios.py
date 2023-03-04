""" Repositorios para el manejo de persistencia de objetos de dominio en la capa de infrastructura del dominio de ordenes

En este archivo usted encontrará las diferentes repositorios para
persistir objetos dominio (agregaciones) en la capa de infraestructura del dominio de ordenes

"""

from eda.config.db import db
from eda.modulos.ordenes.dominio.repositorios import RepositorioReservas, RepositorioProveedores
from eda.modulos.ordenes.dominio.objetos_valor import NombreAero, Odo, Leg, Segmento, Itinerario, CodigoIATA
from eda.modulos.ordenes.dominio.entidades import Proveedor, Aeropuerto, Orden
from eda.modulos.ordenes.dominio.fabricas import FabricaPedido
from .dto import Orden as OrdenDTO
from .mapeadores import MapeadorOrden
from uuid import UUID



class RepositorioOrdenesSQLite(RepositorioReservas):

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

    def agregar(self, reserva: Orden):
        orden_dto = self.fabrica_pedido.crear_objeto(reserva, MapeadorOrden())
        db.session.add(orden_dto)
        db.session.commit()

    def actualizar(self, orden: Orden):
        # TODO
        raise NotImplementedError

    def eliminar(self, orden_id: UUID):
        # TODO
        raise NotImplementedError