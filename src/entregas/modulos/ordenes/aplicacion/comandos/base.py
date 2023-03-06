from entregas.seedwork.aplicacion.comandos import ComandoHandler
from entregas.modulos.ordenes.infraestructura.fabricas import FabricaRepositorio

class EntregarOrdenBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    