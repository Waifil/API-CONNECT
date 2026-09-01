
from flask import Blueprint
from controllers.api_controller import (
    cadastrar_usuario,
    listar_usuarios,
    buscar_usuario
)

api = Blueprint("api", __name__)


@api.route("/usuarios", methods=["POST"])
def cadastrar():
    return cadastrar_usuario()


@api.route("/usuarios", methods=["GET"])
def listar():
    return listar_usuarios()


@api.route("/usuarios/<int:id>", methods=["GET"])
def buscar(id):
    return buscar_usuario(id)

