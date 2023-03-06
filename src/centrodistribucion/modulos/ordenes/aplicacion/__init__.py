from pydispatch import dispatcher

from .handlers import HandlerOrdenIntegracion

from centrodistribucion.modulos.ordenes.dominio.eventos import OrdenAlistada

dispatcher.connect(HandlerOrdenIntegracion.handle_orden_alistada, signal=f'{OrdenAlistada.__name__}Integracion')