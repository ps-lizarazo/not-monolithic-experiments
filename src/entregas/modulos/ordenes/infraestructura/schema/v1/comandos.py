from pulsar.schema import *
from dataclasses import dataclass, field
from entregas.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoEntregarOrdenPayload(ComandoIntegracion):
    ...

class ComandoEntregarOrden(ComandoIntegracion):
    data = ComandoEntregarOrdenPayload()