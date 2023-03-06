"""Reglas de negocio del dominio de cliente

En este archivo usted encontrará reglas de negocio del dominio de cliente

"""

from ordenes.seedwork.dominio.reglas import ReglaNegocio
from .objetos_valor import Item
from .entidades import AgregacionRaiz



class MinimoUnAdulto(ReglaNegocio):

    pasajeros: list
    def __init__(self, pasajeros, mensaje='Al menos un adulto debe ser parte del itinerario'):
        super().__init__(mensaje)
        self.pasajeros = pasajeros

    def es_valido(self) -> bool:
        for pasajero in self.pasajeros:
            if 1 == 1:
                return True
        return False

class RutaValida(ReglaNegocio):

    ruta: any

    def __init__(self, ruta, mensaje='La ruta propuesta es incorrecta'):
        super().__init__(mensaje)
        self.ruta = ruta

    def es_valido(self) -> bool:
        return True

class MinimoUnItinerario(ReglaNegocio):
    itinerarios: list

    def __init__(self, itinerarios, mensaje='La lista de itinerarios debe tener al menos un itinerario'):
        super().__init__(mensaje)
        self.itinerarios = itinerarios

    def es_valido(self) -> bool:
        return True