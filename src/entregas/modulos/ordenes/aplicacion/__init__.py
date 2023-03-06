from pydispatch import dispatcher

from .handlers import HandlerOrdenIntegracion

from entregas.modulos.ordenes.dominio.eventos import OrdenEntregada

dispatcher.connect(HandlerOrdenIntegracion.handle_orden_entregada, signal=f'{OrdenEntregada.__name__}Integracion')