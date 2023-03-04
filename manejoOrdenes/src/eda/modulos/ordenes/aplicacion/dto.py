from dataclasses import dataclass, field
from eda.seedwork.aplicacion.dto import DTO



@dataclass(frozen=True)
class ItemDTO(DTO):
    id: str 
    nombre: str 
    cantidad: int
    peso: float
    tamanio: float
    direccion_recogida: dict
    direccion_entrega: dict

@dataclass(frozen=True)
class OrdenDTO(DTO):
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    id: str = field(default_factory=str)
    items: list[ItemDTO] = field(default_factory=list)