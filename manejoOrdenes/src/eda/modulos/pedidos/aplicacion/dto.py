from dataclasses import dataclass, field
from eda.seedwork.aplicacion.dto import DTO



@dataclass(frozen=True)
class ItemDTO(DTO):
    id: str
    nombre:str
    cantidad:int
    pais_recogida:str
    ciudad_recogida:str
    direccion_recogida:str
    codigo_postal_recogida:str
    telefono_responsable_recogida:str
    nombre_responsable_recogida:str
    pais_entrega:str
    ciudad_entrega:str
    direccion_entrega:str
    codigo_postal_entrega:str
    telefono_responsable_entrega:str
    nombre_responsable_entrega:str

@dataclass(frozen=True)
class OrdenDTO(DTO):
    id: str = field(default_factory=str)
    fecha_creacion: str = field(default_factory=str)
    fecha_actualizacion: str = field(default_factory=str)
    items: list[ItemDTO] = field(default_factory=list)