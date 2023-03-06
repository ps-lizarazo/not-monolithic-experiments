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
    publicador = cliente.create_producer(topico, schema=AvroSchema(ComandoCrearOrden))
    publicador.send(mensaje)
    print("===========EVENTO ENVIADO============")
    cliente.close()


class ComandoIntegracion(Record):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()

class ComandoCrearOrdenItem(Record):
    direccion_recogida = String()
    direccion_entrega = String()
    tamanio = String()
    telefono = String()

class ComandoCrearOrdenPayload(Record):
    items = Array(ComandoCrearOrdenItem())

class ComandoCrearOrden(ComandoIntegracion):
    id = String(default=str(uuid.uuid4()))
    time = Long()
    ingestion = Long(default=time_millis())
    specversion = String()
    type = String()
    datacontenttype = String()
    service_name = String()
    data = ComandoCrearOrdenPayload()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

new_command = ComandoCrearOrden(
    data= ComandoCrearOrdenPayload (
        guid=str(uuid.uuid4()),
        items= [
            ComandoCrearOrdenItem (
                direccion_recogida = "Av direccion recoger 123",
                direccion_entrega = "Av para entregar 123",
                tamanio = "5kg",
                telefono = "300 321321",
            ),
        ],
        fecha_creacion=int(datetime.now().timestamp())
    )
)

_publicar_mensaje(new_command, 'comandos-orden', AvroSchema(ComandoCrearOrden))
