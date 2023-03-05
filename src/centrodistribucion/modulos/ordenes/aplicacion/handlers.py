from centrodistribucion.modulos.ordenes.dominio.eventos import OrdenAlistada
from centrodistribucion.seedwork.aplicacion.handlers import Handler
from centrodistribucion.modulos.ordenes.infraestructura.despachadores import Despachador

class HandlerOrdenIntegracion(Handler):
    @staticmethod
    def handle_orden_alistada(evento):
        despachador = Despachador()
        despachador.publicar_evento(evento, 'eventos-centrodistribucion')