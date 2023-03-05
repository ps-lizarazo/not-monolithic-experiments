from abc import ABC
from centrodistribucion.seedwork.dominio.repositorios import Repositorio

class RepositorioOrdenes(Repositorio, ABC):
    ...

class RepositorioEventosOrdenes(Repositorio, ABC):
    ...