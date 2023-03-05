import pulsar
from pulsar.schema import *
from dataclasses import dataclass
from datetime import datetime
import uuid
import time

def time_millis():
    return int(time.time() * 1000)

def _publicar_mensaje(mensaje, topico, schema):
    cliente = pulsar.Client('pulsar://localhost:6650')
    publicador = cliente.create_producer(topico, schema=AvroSchema(EventoOrdenCreada))
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

class EventoOrdenCreadaPayload(Record):
    id_reserva = String()
    id_cliente = String()
    estado = String()
    fecha_creacion = Long()

class EventoOrdenCreada(EventoIntegracion):
    # NOTE La librería Record de Pulsar no es capaz de reconocer campos heredados, 
    # por lo que los mensajes al ser codificados pierden sus valores
    # Dupliqué el los cambios que ya se encuentran en la clase Mensaje
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = EventoOrdenCreadaPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

new_event = EventoOrdenCreada(
    data=EventoOrdenCreadaPayload(
        id_reserva=str('123'),
        id_cliente=str('456'),
        estado=str('CREADA'),
        fecha_creacion=int(datetime.now().timestamp())
    )
)

_publicar_mensaje(new_event, 'eventos-orden', AvroSchema(EventoOrdenCreada))