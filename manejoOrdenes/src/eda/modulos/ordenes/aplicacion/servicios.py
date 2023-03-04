from eda.seedwork.aplicacion.servicios import Servicio
from eda.modulos.ordenes.dominio.entidades import Orden
from eda.modulos.ordenes.dominio.fabricas import FabricaOrdenes
from eda.modulos.ordenes.infraestructura.fabricas import FabricaRepositorio
from eda.modulos.ordenes.infraestructura.repositorios import RepositorioReservas
from ..infraestructura.mapeadores import MapeadorOrden

from .dto import OrdenDTO


class ServicioOrdenes(Servicio):

	def __init__(self):
		self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
		self._fabrica_ordenes: FabricaOrdenes = FabricaOrdenes()

	@property
	def fabrica_repositorio(self):
		return self._fabrica_repositorio

	@property
	def fabrica_orden(self):
		return self._fabrica_ordenes

	def crear_orden(self, orden_dto: OrdenDTO) -> OrdenDTO:
		reserva: Orden = self.fabrica_orden.crear_objeto(
			orden_dto, MapeadorOrden())

		repositorio = self.fabrica_repositorio.crear_objeto(
			RepositorioReservas.__class__)
		repositorio.agregar(reserva)

		return self.fabrica_orden.crear_objeto(reserva, MapeadorOrden())

	def obtener_reserva_por_id(self, id) -> OrdenDTO:
		repositorio = self.fabrica_repositorio.crear_objeto(
			RepositorioReservas.__class__)
		return repositorio.obtener_por_id(id).__dict__
