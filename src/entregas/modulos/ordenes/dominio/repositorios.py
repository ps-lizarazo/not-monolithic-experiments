from abc import ABC
from entregas.seedwork.dominio.repositorios import Repositorio

class RepositorioOrdenes(Repositorio, ABC):
    ...

class RepositorioEventosOrdenes(Repositorio, ABC):
    ...