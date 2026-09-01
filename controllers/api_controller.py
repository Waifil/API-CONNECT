
from flask import request, jsonify
from data.database import usuarios, criar_usuario


def cadastrar_usuario():
    dados = request.get_json()

    if not dados:
        return jsonify({
            "error": "Os dados do usuário são obrigatórios."
        }), 400

    if not dados.get("nome"):
        return jsonify({
            "error": "O campo 'nome' é obrigatório."
        }), 400

    if not dados.get("email"):
        return jsonify({
            "error": "O campo 'email' é obrigatório."
        }), 400

    usuario = criar_usuario(
        dados["nome"],
        dados["email"]
    )

    return jsonify({
        "data": usuario
    }), 201


def listar_usuarios():
    return jsonify({
        "data": usuarios
    }), 200


def buscar_usuario(id):
    for usuario in usuarios:
        if usuario["id"] == id:
            return jsonify({
                "data": usuario
            }), 200

    return jsonify({
        "error": "Usuário não encontrado"
    }), 404


