import pulsar
from pulsar.schema import *
from dataclasses import dataclass
from datetime import datetime
import uuid
import time

def time_millis():
    return int(time.time() * 1000)

def _publicar_mensaje(mensaje, topico, schema):
    token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5rRXdSVVU1TUVOQlJrWTJNalEzTVRZek9FVkZRVVUyT0RNME5qUkRRVEU1T1VNMU16STVPUSJ9.eyJodHRwczovL3N0cmVhbW5hdGl2ZS5pby91c2VybmFtZSI6Im5vLW1vbm9saXRvcy1hY2NvdW50QG8tdmJrcnAuYXV0aC5zdHJlYW1uYXRpdmUuY2xvdWQiLCJpc3MiOiJodHRwczovL2F1dGguc3RyZWFtbmF0aXZlLmNsb3VkLyIsInN1YiI6Ik96OGNZUzlTSDZyb3NBNWNleG1BbTJOVlpsMzFXeGRrQGNsaWVudHMiLCJhdWQiOiJ1cm46c246cHVsc2FyOm8tdmJrcnA6Y2x1c3Rlci11IiwiaWF0IjoxNjc4MzQ1NTk0LCJleHAiOjE2Nzg5NTAzOTQsImF6cCI6Ik96OGNZUzlTSDZyb3NBNWNleG1BbTJOVlpsMzFXeGRrIiwic2NvcGUiOiJhZG1pbiBhY2Nlc3MiLCJndHkiOiJjbGllbnQtY3JlZGVudGlhbHMiLCJwZXJtaXNzaW9ucyI6WyJhZG1pbiIsImFjY2VzcyJdfQ.DUW-F4QecOtmtwGUMdeYXGyUHcoq9DCX3u0m_Y9oJJyLXq5wFZCU2MSyvuqXc5myC3BcKxEsDho9q8JuKNexMLzA8I8x71MKw4AV9uQlRXIuYV2jGoVolIZ-2B6HhrxVquOeRfWpw1VGFYDOR1_qMR57W_yqCnXqXarS2O7tALEK3Q_9mCFSvJX0fu8TnGgdvJhxOR4Rsirn14WFVVt1AQg85Wre-YP_AKcRZocxshx7AwhfWLjMu6EmoLGKh1KlB1W4sqXjzuWywuC7zjCPPZquL40Kt6poKLhgRXmgRfk8FlhlZls-fkh6BQvJC5m71uuGbKgHgGGHyXHy1zbRrw'
    cliente = pulsar.Client(
        'pulsar+ssl://cluster-u-479cbdfd-93b9-4b83-8f6f-e694b327fe7c.gcp-shared-gcp-usce1-martin.streamnative.g.snio.cloud:6651', authentication=pulsar.AuthenticationToken(token))
    #cliente = pulsar.Client(f'pulsar://{utils.broker_host()}:6650')
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
                direccion_recogida = "Calle falsa 123",
                direccion_entrega = "Calle falsa 123",
                tamanio = "5kg",
                telefono = "300 321321",
            ),
        ],
        fecha_creacion=int(datetime.now().timestamp())
    )
)

_publicar_mensaje(new_command, 'comandos-orden', AvroSchema(ComandoCrearOrden))
