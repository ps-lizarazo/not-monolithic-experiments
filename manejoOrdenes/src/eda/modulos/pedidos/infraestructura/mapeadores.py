""" Mapeadores para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from eda.seedwork.dominio.repositorios import Mapeador
from eda.modulos.pedidos.dominio.objetos_valor import  Item
from eda.modulos.pedidos.dominio.entidades import Orden
from .dto import Orden as OrdenDTO
from .dto import Item as ItemDTO

class MapeadorOrden(Mapeador):
	_FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

	def _procesar_items_dto(self, items_dto: list) -> list[Item]:
		
		items: list[Item] = []
		for item_param in items_dto:
			item: Item
			_direccion_recogida = item_param.direccion_recogida
			_direccion_entrega = item_param.direccion_entrega
			
			item.id = item_param.id
			item.nombre = item_param.name
			item.cantidad =  item_param.cantidad
			item.pais_recogida = _direccion_recogida.pais
			item.ciudad_recogida =_direccion_recogida.ciudad
			item.direccion_recogida = _direccion_recogida.direccion
			item.codigo_postal_recogida = _direccion_recogida.codigo_postal
			item.telefono_responsable_recogida = _direccion_recogida.telefono_responsable
			item.nombre_responsable_recogida = _direccion_recogida.nombre_responsable
			item.pais_entrega = _direccion_entrega.pais
			item.ciudad_entrega =_direccion_entrega.ciudad
			item.direccion_entrega = _direccion_entrega.direccion
			item.codigo_postal_entrega = _direccion_entrega.codigo_postal
			item.telefono_responsable_entrega = _direccion_entrega.telefono_responsable
			item.nombre_responsable_entrega = _direccion_entrega.nombre_responsable

			items.append(item)

		return items

	def _procesar_item(self, item: any) -> list[ItemDTO]:
		items_dto = list()
		
		item_dto = ItemDTO()
		item_dto.id = item.id
		item_dto.nombre = item.nombre
		item_dto.cantidad = item.cantidad
		item_dto.pais_recogida = item.pais_recogida
		item_dto.ciudad_recogida = item.ciudad_recogida
		item_dto.direccion_recogida = item.direccion_recogida
		item_dto.codigo_postal_recogida = item.codigo_postal_recogida
		item_dto.telefono_responsable_recogida = item.telefono_responsable_recogida
		item_dto.nombre_responsable_recogida = item.nombre_responsable_recogida
		item_dto.pais_entrega = item.pais_entrega
		item_dto.ciudad_entrega = item.ciudad_entrega
		item_dto.direccion_entrega = item.direccion_entrega
		item_dto.codigo_postal_entrega = item.codigo_postal_entrega
		item_dto.telefono_responsable_entrega = item.telefono_responsable_entrega
		item_dto.nombre_responsable_entrega = item.nombre_responsable_entrega		

		items_dto.append(item_dto)

		return items_dto

	def obtener_tipo(self) -> type:
		return Orden.__class__

	def entidad_a_dto(self, entidad: Orden) -> OrdenDTO:
			
		orden_dto = OrdenDTO()
		orden_dto.fecha_creacion = entidad.fecha_creacion
		orden_dto.fecha_actualizacion = entidad.fecha_actualizacion
		orden_dto.id = str(entidad.id)

		items_dto = list()
		
		for item in entidad.items:
				items_dto.extend(self._procesar_item(item))

		orden_dto.items = items_dto

		return orden_dto

	def dto_a_entidad(self, dto: OrdenDTO) -> Orden:
		orden = Orden(dto.id, dto.fecha_creacion, dto.fecha_actualizacion)
		orden.items = list()

		items_dto: list[ItemDTO] = dto.items

		orden.items.extend(self._procesar_items_dto(items_dto))
		
		return orden