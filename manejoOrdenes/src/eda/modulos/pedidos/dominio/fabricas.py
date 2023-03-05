""" Fábricas para la creación de objetos del dominio de vuelos

En este archivo usted encontrará las diferentes fábricas para crear
objetos complejos del dominio de vuelos

"""

from .entidades import Orden
from .reglas import MinimoUnItinerario, RutaValida
from .excepciones import TipoObjetoNoExisteEnDominioVuelosExcepcion
from eda.seedwork.dominio.repositorios import Mapeador, Repositorio
from eda.seedwork.dominio.fabricas import Fabrica
from eda.seedwork.dominio.entidades import Entidad
from dataclasses import dataclass
import pdb
@dataclass
class _FabricaOrdenes(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if isinstance(obj, Entidad):
            return mapeador.entidad_a_dto(obj)
        else:
            
            orden: Orden = mapeador.dto_a_entidad(obj)

            self.validar_regla(MinimoUnItinerario(orden.items))
            #[self.validar_regla(RutaValida(ruta)) for itin in orden.items for odo in itin.odos for segmento in odo.segmentos for ruta in segmento.legs]
            
            return orden

@dataclass
class FabricaPedido(Fabrica):
    def crear_objeto(self, obj: any, mapeador: Mapeador) -> any:
        if mapeador.obtener_tipo() == Orden.__class__:
            fabrica_orden = _FabricaOrdenes()
            return fabrica_orden.crear_objeto(obj, mapeador)
        else:
            raise TipoObjetoNoExisteEnDominioVuelosExcepcion()

