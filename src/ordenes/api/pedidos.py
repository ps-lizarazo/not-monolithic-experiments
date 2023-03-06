import ordenes.seedwork.presentacion.api as api
import json
from ordenes.modulos.pedidos.aplicacion.servicios import ServicioOrdenes
from ordenes.modulos.pedidos.aplicacion.dto import OrdenDTO
from ordenes.seedwork.dominio.excepciones import ExcepcionDominio

from flask import redirect, render_template, request, session, url_for
from flask import Response
from ordenes.modulos.pedidos.aplicacion.mapeadores import MapeadorOrdenDTOJson
import pdb

bp = api.crear_blueprint('pedidos', '/pedidos')

@bp.route('/orden', methods=('POST',))
def reservar():
    try:
        
        orden_dict = request.json

        map_orden = MapeadorOrdenDTOJson()
        orden_dto = map_orden.externo_a_dto(orden_dict)

        sr = ServicioOrdenes()
        dto_final = sr.crear_orden(orden_dto)

        return map_orden.dto_a_externo(dto_final)
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

@bp.route('/orden', methods=('GET',))
@bp.route('/orden/<id>', methods=('GET',))
def dar_reserva(id=None):
    if id:
        sr = ServicioOrdenes()
        
        return sr.obtener_reserva_por_id(id)
    else:
        return [{'message': 'GET!'}]

@bp.route("/health-ordenes", methods=('GET',))
def health():
  return {"status": "up-ordenes"}