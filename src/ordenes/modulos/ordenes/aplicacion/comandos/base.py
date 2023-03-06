from ordenes.seedwork.aplicacion.comandos import ComandoHandler
from ordenes.modulos.ordenes.infraestructura.fabricas import FabricaRepositorio

class CrearOrdenBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    