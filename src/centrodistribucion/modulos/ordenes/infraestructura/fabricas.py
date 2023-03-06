""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de ordenes

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de ordenes

"""

from dataclasses import dataclass, field
from centrodistribucion.seedwork.dominio.fabricas import Fabrica
from centrodistribucion.seedwork.dominio.repositorios import Repositorio
from centrodistribucion.modulos.ordenes.dominio.repositorios import RepositorioOrdenes, RepositorioEventosOrdenes
from .repositorios import RepositorioOrdenesSQLAlchemy, RepositorioEventosOrdenesSQLAlchemy
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioOrdenes:
            return RepositorioOrdenesSQLAlchemy()
        elif obj == RepositorioEventosOrdenes:
            return RepositorioEventosOrdenesSQLAlchemy()
        else:
            raise ExcepcionFabrica(f'No existe fábrica para el objeto {obj}')