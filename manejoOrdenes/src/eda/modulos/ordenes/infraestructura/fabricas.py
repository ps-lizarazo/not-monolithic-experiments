""" Fábricas para la creación de objetos en la capa de infrastructura del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos en la capa de infraestructura del dominio de vuelos

"""

from dataclasses import dataclass, field
from eda.seedwork.dominio.fabricas import Fabrica
from eda.seedwork.dominio.repositorios import Repositorio
from eda.modulos.ordenes.dominio.repositorios import RepositorioOrdenes, RepositorioItems
from .repositorios import RepositorioReservasSQLite, RepositorioProveedoresSQLite
from .excepciones import ExcepcionFabrica

@dataclass
class FabricaRepositorio(Fabrica):
    def crear_objeto(self, obj: type, mapeador: any = None) -> Repositorio:
        if obj == RepositorioOrdenes.__class__:
            return RepositorioReservasSQLite()
        elif obj == RepositorioItems.__class__:
            return RepositorioProveedoresSQLite()
        else:
            raise ExcepcionFabrica()