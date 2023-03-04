import pulsar
from pulsar.schema import *
from dataclasses import dataclass
from datetime import datetime
import uuid
import time

def time_millis():
    return int(time.time() * 1000)

def _publicar_mensaje(mensaje, topico, schema):
    cliente = pulsar.Client('pulsar://host.docker.internal:6650')
    publicador = cliente.create_producer(topico, schema=AvroSchema(EventoReservaCreada))
    publicador.send(mensaje)
    cliente.close()


class EventoIntegracion(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()

class ReservaCreadaPayload(Record):
    id_reserva = String()
    id_cliente = String()
    estado = String()
    fecha_creacion = Long()

class EventoReservaCreada(EventoIntegracion):
    data = ReservaCreadaPayload()

new_event = EventoReservaCreada(
    id=str(uuid.uuid4()),
    time=int(datetime.now().timestamp()),
    ingestion=int(datetime.now().timestamp()),
    specversion='1.0',
    type='ReservaCreada',
    datacontenttype='application/json',
    service_name='centrodistribucion',
    data=ReservaCreadaPayload(
        id_reserva='123',
        id_cliente='456',
        estado='CREADA',
        fecha_creacion=int(datetime.now().timestamp())
    )
)

_publicar_mensaje(new_event, 'eventos-orden', AvroSchema(EventoReservaCreada))