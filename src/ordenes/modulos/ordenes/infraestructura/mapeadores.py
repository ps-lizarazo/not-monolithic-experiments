from ordenes.modulos.ordenes.dominio.eventos import OrdenCreada
from ordenes.modulos.ordenes.infraestructura.schema.v1.eventos import EventoOrdenCreada, EventoOrdenCreadaPayload, EventoOrdenCreadaItem


def EventoDominioAIntegracion(evento: OrdenCreada) -> EventoOrdenCreada:
    return EventoOrdenCreada(
        data=EventoOrdenCreadaPayload(
            guid=evento.guid,
            items=[
                EventoOrdenCreadaItem(
                    guid=item.guid,
                    direccion_recogida=item.direccion_recogida,
                    direccion_entrega=item.direccion_entrega,
                    tamanio=item.tamanio,
                    telefono=item.telefono
                ) for item in evento.items
            ],
            fecha_creacion=int(evento.fecha_creacion)
        )
    )
