from pulsar.schema import *
from dataclasses import dataclass, field
from centrodistribucion.seedwork.infraestructura.schema.v1.comandos import (ComandoIntegracion)

class ComandoAlistarOrdenPayload(ComandoIntegracion):
    ...

class ComandoAlistarOrden(ComandoIntegracion):
    data = ComandoAlistarOrdenPayload()