import pulsar
from pulsar.schema import *
from dataclasses import dataclass
from datetime import datetime
import uuid
import time

def time_millis():
    return int(time.time() * 1000)

def _consumir_mensajes(topico, schema):
    cliente = pulsar.Client('pulsar://localhost:6650')
    consumidor = cliente.subscribe(topico, subscription_name="entregas-sub-eventos", schema=AvroSchema(EventoOrdenAlistada))
    
    while True:
        mensaje = consumidor.receive()
        print(f'Evento recibido: {mensaje.value().data}')

        consumidor.acknowledge(mensaje)

class EventoIntegracion(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()

class EventoOrdenAlistadaItem(Record):
    guid = String()
    direccion_centro_distribucion = String()
    direccion_entrega = String()
    tamanio = String()
    telefono = String()

class EventoOrdenAlistadaPayload(Record):
    guid = String()
    items = Array(EventoOrdenAlistadaItem())
    fecha_creacion = Long()

class EventoOrdenAlistada(EventoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = EventoOrdenAlistadaPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

_consumir_mensajes('eventos-centrodistribucion', AvroSchema(EventoOrdenAlistada))
