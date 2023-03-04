from eda.seedwork.aplicacion.dto import Mapeador as AppMap
from eda.seedwork.dominio.repositorios import Mapeador as RepMap
from eda.modulos.ordenes.dominio.entidades import Orden
from eda.modulos.ordenes.dominio.objetos_valor import Item
from .dto import OrdenDTO, ItemDTO

from datetime import datetime

class MapeadorOrdenDTOJson(AppMap):
    def _procesar_item(self, item: dict) -> ItemDTO:

        item_dto: ItemDTO = ItemDTO(item.get('nombre'), item.get('cantidad'), item.get('origen'), item.get('destino')) 
        return item_dto
    
    def externo_a_dto(self, externo: dict) -> OrdenDTO:
        orden_dto = OrdenDTO()

        items: list[ItemDTO] = list()
        for itin in externo.get('items', list()):
            orden_dto.items.append(self._procesar_item(itin))

        return orden_dto

    def dto_a_externo(self, dto: OrdenDTO) -> dict:
        return dto.__dict__

class MapeadorOrdenes(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def _procesar_itinerario(self, item_dto: ItemDTO) -> Item:
        Item()
        odos = list()

        for odo_dto in itinerario_dto.odos:
            segmentos = list()
            for seg_dto in odo_dto.segmentos:
                
                legs = list()

                for leg_dto in seg_dto.legs:
                    destino = Aeropuerto(codigo=leg_dto.destino.get('codigo'), nombre=leg_dto.destino.get('nombre'))
                    origen = Aeropuerto(codigo=leg_dto.origen.get('codigo'), nombre=leg_dto.origen.get('nombre'))
                    fecha_salida = datetime.strptime(leg_dto.fecha_salida, self._FORMATO_FECHA)
                    fecha_llegada = datetime.strptime(leg_dto.fecha_llegada, self._FORMATO_FECHA)

                    leg: Leg = Leg(fecha_salida, fecha_llegada, origen, destino)

                    legs.append(leg)

                segmentos.append(Segmento(legs))
            
            odos.append(Odo(segmentos))

        return Item(odos)

    def obtener_tipo(self) -> type:
        return Orden.__class__


    def entidad_a_dto(self, entidad: Orden) -> OrdenDTO:
        
        fecha_creacion = entidad.fecha_creacion.strftime(self._FORMATO_FECHA)
        fecha_actualizacion = entidad.fecha_actualizacion.strftime(self._FORMATO_FECHA)
        _id = str(entidad.id)

        return OrdenDTO(fecha_creacion, fecha_actualizacion, _id, list())

    def dto_a_entidad(self, dto: OrdenDTO) -> Orden:
        reserva = Orden()
        reserva.itinerarios = list()

        itinerarios_dto: list[ItemDTO] = dto.itinerarios

        for itin in itinerarios_dto:
            reserva.itinerarios.append(self._procesar_itinerario(itin))
        
        return reserva



