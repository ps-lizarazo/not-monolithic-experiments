"""Objetos valor reusables parte del seedwork del proyecto

En este archivo usted encontrará los objetos valor reusables parte del seedwork del proyecto

"""

from dataclasses import dataclass
from abc import ABC, abstractmethod
from .entidades import Locacion
from datetime import datetime

@dataclass(frozen=True)
class ObjetoValor:
    ...

@dataclass(frozen=True)
class Codigo(ABC, ObjetoValor):
    codigo: str

class Direccion(ABC, ObjetoValor):
    @abstractmethod
    def pais(self) -> str:
        ...
    
    @abstractmethod
    def ciudad(self) -> str:
        ...
    
    @abstractmethod
    def direccion(self) -> str:
        ...

    @abstractmethod
    def codigo_postal(self) -> str:
        ...

    @abstractmethod
    def telefono_responsable(self) -> str:
        ...

    @abstractmethod
    def nombre_responsable(self) -> str:
        ...



