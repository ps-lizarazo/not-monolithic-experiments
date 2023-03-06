from entregas.modulos.ordenes.dominio.eventos import OrdenEntregada
from entregas.seedwork.aplicacion.handlers import Handler
from entregas.modulos.ordenes.infraestructura.despachadores import Despachador

class HandlerOrdenIntegracion(Handler):
    @staticmethod
    def handle_orden_entregada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-entregas')