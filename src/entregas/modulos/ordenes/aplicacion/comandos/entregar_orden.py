from entregas.seedwork.aplicacion.comandos import Comando
from .base import EntregarOrdenBaseHandler
from dataclasses import dataclass, field
from entregas.seedwork.aplicacion.comandos import ejecutar_commando as comando
from typing import List

from entregas.modulos.ordenes.dominio.entidades import Orden, OrdenItems
from entregas.seedwork.infraestructura.uow import UnidadTrabajoPuerto
from entregas.modulos.ordenes.dominio.repositorios import RepositorioOrdenes, RepositorioEventosOrdenes

@dataclass
class EntregarOrdenItems:
    guid: str = None
    fecha_entrega: str = None
    direccion_entrega: str = None
    persona_recibe: str = None
    mecanismo_entrega: str = None

@dataclass
class EntregarOrden(Comando):
    guid: str = None
    fecha_creacion: str = None
    items: List[EntregarOrdenItems] = None

class EntregarOrdenHandler(EntregarOrdenBaseHandler):
    
    def handle(self, comando: EntregarOrden):
        orden: Orden = Orden (
            guid=comando.guid,
            fecha_creacion=comando.fecha_creacion,
            items=[
                OrdenItems(
                    guid=item.guid,
                    fecha_entrega=item.fecha_entrega,
                    direccion_entrega=item.direccion_entrega,
                    persona_recibe=item.persona_recibe,
                    mecanismo_entrega=item.mecanismo_entrega,
                ) for item in comando.items
            ]
        )

        orden.entregar_orden(orden)
        # Escribe en las tablas el evento y el objeto
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioOrdenes)
        repositorio_eventos = self.fabrica_repositorio.crear_objeto(RepositorioEventosOrdenes)

        UnidadTrabajoPuerto.registrar_batch(repositorio.agregar, orden, repositorio_eventos_func=repositorio_eventos.agregar)
        UnidadTrabajoPuerto.commit()
        UnidadTrabajoPuerto.clean_session()

@comando.register(EntregarOrden)
def ejecutar_comando_alistar_orden(comando: EntregarOrden):
    handler = EntregarOrdenHandler()
    handler.handle(comando)
    