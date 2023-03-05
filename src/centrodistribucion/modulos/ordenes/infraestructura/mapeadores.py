from centrodistribucion.modulos.ordenes.dominio.eventos import OrdenAlistada
from centrodistribucion.modulos.ordenes.infraestructura.schema.v1.eventos import EventoOrdenAlistada, EventoOrdenAlistadaPayload, EventoOrdenAlistadaItem


def EventoDominioAIntegracion(evento: OrdenAlistada) -> EventoOrdenAlistada:
    return EventoOrdenAlistada(
        data=EventoOrdenAlistadaPayload(
            guid=evento.guid,
            items=[
                EventoOrdenAlistadaItem(
                    guid=item.guid,
                    direccion_centro_distribucion=item.direccion_centro_distribucion,
                    direccion_entrega=item.direccion_entrega,
                    tamanio=item.tamanio,
                    telefono=item.telefono
                ) for item in evento.items
            ],
            fecha_creacion=int(evento.fecha_creacion)
        )
    )
