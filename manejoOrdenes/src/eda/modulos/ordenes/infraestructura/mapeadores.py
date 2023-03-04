""" Mapeadores para la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará los diferentes mapeadores
encargados de la transformación entre formatos de dominio y DTOs

"""

from eda.seedwork.dominio.repositorios import Mapeador
from eda.modulos.ordenes.dominio.objetos_valor import NombreAero, Odo, Leg, Segmento, Item, CodigoIATA
from eda.modulos.ordenes.dominio.entidades import Proveedor, Aeropuerto, Orden
from .dto import Orden as OrdenDTO
from .dto import Item as ItemDTO

class MapeadorOrden(Mapeador):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_items_dto(self, items_dto: list) -> list[Item]:
       
        return [Item]

    def _procesar_itinerario(self, item: any) -> list[ItemDTO]:
        items_dto = list()

        
        item_dto = ItemDTO()
        item_dto.nombre = item.nombre
        item_dto.origen_codigo = leg.origen.codigo
        item_dto.fecha_salida = leg.fecha_salida
        item_dto.fecha_llegada = leg.fecha_llegada
        item_dto.leg_orden = k
        item_dto.segmento_orden = j
        item_dto.odo_orden = i

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
            items_dto.extend(self._procesar_itinerario(item))

        orden_dto.items = items_dto

        return orden_dto

    def dto_a_entidad(self, dto: OrdenDTO) -> Orden:
        orden = Orden(dto.id, dto.fecha_creacion, dto.fecha_actualizacion)
        orden.items = list()

        items_dto: list[ItemDTO] = dto.items

        orden.items.extend(self._procesar_items_dto(items_dto))
        
        return orden