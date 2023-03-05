from eda.seedwork.aplicacion.dto import Mapeador as AppMap
from eda.seedwork.dominio.repositorios import Mapeador as RepMap
from eda.modulos.pedidos.dominio.entidades import Orden
from eda.modulos.pedidos.dominio.objetos_valor import Item
from .dto import OrdenDTO, ItemDTO

from datetime import datetime
import pdb
class MapeadorOrdenDTOJson(AppMap):
    def _procesar_item(self, item_pram: dict) -> ItemDTO:
        _direccion_recogida = item_pram.get('direccion_recogida')
        _direccion_entrega = item_pram.get('direccion_entrega')
        
        item: ItemDTO = ItemDTO(
            item_pram.get('nombre'),
            item_pram.get('cantidad'),
            _direccion_recogida.get('pais'),
            _direccion_recogida.get('ciudad'),
            _direccion_recogida.get('direccion'),
            _direccion_recogida.get('codigo_postal'),
            _direccion_recogida.get('telefono_responsable'),
            _direccion_recogida.get('nombre_responsable'),
            _direccion_entrega.get('pais'),
            _direccion_entrega.get('ciudad'),
            _direccion_entrega.get('direccion'),
            _direccion_entrega.get('codigo_postal'),
            _direccion_entrega.get('telefono_responsable'),
            _direccion_entrega.get('nombre_responsable')
        )
        return item
    
    def externo_a_dto(self, externo: dict) -> OrdenDTO:
        orden_dto = OrdenDTO()

        items: list[ItemDTO] = list()
        for itm in externo.get('orden').get('items', list()):
            orden_dto.items.append(self._procesar_item(itm))
    
        return orden_dto

    def dto_a_externo(self, dto: OrdenDTO) -> dict:
        return dto.__dict__

class MapeadorOrdenes(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_item(self, item_dto: ItemDTO) -> Item:
        
        Item(
            item_dto.nombre,
            item_dto.cantidad,
            item_dto.pais_recogida,
            item_dto.ciudad_recogida,
            item_dto.direccion_recogida,
            item_dto.codigo_postal_recogida,
            item_dto.telefono_responsable_recogida,
            item_dto.nombre_responsable_recogida,
            item_dto.pais_entrega,
            item_dto.ciudad_entrega,
            item_dto.direccion_entrega,
            item_dto.codigo_postal_entrega,
            item_dto.telefono_responsable_entrega,
            item_dto.nombre_responsable_entrega
        )
        
        return Item

    def obtener_tipo(self) -> type:
        return Orden.__class__


    def entidad_a_dto(self, entidad: Orden) -> OrdenDTO:
        
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)

        return OrdenDTO(fecha_creacion, fecha_actualizacion, _id, list())

    def dto_a_entidad(self, dto: OrdenDTO) -> Orden:
        orden = Orden()
        orden.items = list()

        items_dto: list[ItemDTO] = dto.items

        for itm in items_dto:
            orden.items.append(self._procesar_item(itm))
        
        return orden



