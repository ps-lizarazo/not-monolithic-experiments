import eda.seedwork.presentacion.api as api
import json
from eda.modulos.ordenes.aplicacion.servicios import ServicioReserva
from eda.modulos.ordenes.aplicacion.dto import OrdenDTO
from eda.seedwork.dominio.excepciones import ExcepcionDominio

from flask import redirect, render_template, request, session, url_for
from flask import Response
from eda.modulos.ordenes.aplicacion.mapeadores import MapeadorReservaDTOJson

bp = api.crear_blueprint('ordenes', '/ordenes')

@bp.route('/orden', methods=('POST',))
def reservar():
    try:
        reserva_dict = request.json

        map_reserva = MapeadorReservaDTOJson()
        reserva_dto = map_reserva.externo_a_dto(reserva_dict)

        sr = ServicioReserva()
        dto_final = sr.crear_reserva(reserva_dto)

        return map_reserva.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/orden', methods=('GET',))
@bp.route('/orden/<id>', methods=('GET',))
def dar_reserva(id=None):
    if id:
        sr = ServicioReserva()
        
        return sr.obtener_reserva_por_id(id)
    else:
        return [{'message': 'GET!'}]