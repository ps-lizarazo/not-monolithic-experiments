from entregas.modulos.ordenes.dominio.eventos import OrdenEntregada
from entregas.modulos.ordenes.infraestructura.schema.v1.eventos import EventoOrdenEntregada, EventoOrdenEntregadaPayload, EventoOrdenEntregadaItem
from datetime import datetime


def EventoDominioAIntegracion(evento: OrdenEntregada) -> EventoOrdenEntregada:
    return EventoOrdenEntregada(
        data=EventoOrdenEntregadaPayload(
            guid=evento.guid,
            items=[
                EventoOrdenEntregadaItem(
                    guid=item.guid,
                    fecha_entrega=int(datetime.fromisoformat(item.fecha_entrega).timestamp()),
                    direccion_entrega=item.direccion_entrega,
                    persona_recibe=item.persona_recibe,
                    mecanismo_entrega=item.mecanismo_entrega
                ) for item in evento.items
            ],
            fecha_creacion=int(evento.fecha_creacion)
        )
    )
