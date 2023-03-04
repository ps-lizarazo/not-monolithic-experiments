from eda.seedwork.aplicacion.servicios import Servicio
from eda.modulos.pedidos.dominio.entidades import Orden
from eda.modulos.pedidos.dominio.fabricas import FabricaPedido
from eda.modulos.pedidos.infraestructura.fabricas import FabricaRepositorio
from eda.modulos.pedidos.infraestructura.repositorios import RepositorioOrdenes
from ..infraestructura.mapeadores import MapeadorOrden

from .dto import OrdenDTO


class ServicioOrdenes(Servicio):

	def __init__(self):
		self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
		self._fabrica_pedido: FabricaPedido = FabricaPedido()

	@property
	def fabrica_repositorio(self):
		return self._fabrica_repositorio

	@property
	def fabrica_orden(self):
		return self._fabrica_pedido

	def crear_orden(self, orden_dto: OrdenDTO) -> OrdenDTO:
		orden: Orden = self.fabrica_orden.crear_objeto(orden_dto, MapeadorOrden())

		repositorio = self.fabrica_repositorio.crear_objeto(RepositorioOrdenes.__class__)
		repositorio.agregar(orden)

		return self.fabrica_orden.crear_objeto(orden, MapeadorOrden())

	def obtener_orden_por_id(self, id) -> OrdenDTO:
		repositorio = self.fabrica_repositorio.crear_objeto(
			RepositorioOrdenes.__class__)
		return repositorio.obtener_por_id(id).__dict__
