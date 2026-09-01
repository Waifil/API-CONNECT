
usuarios = []



proximo_id = 1


def criar_usuario(nome, email):
    global proximo_id

    usuario = {
        "id": proximo_id,
        "nome": nome,
        "email": email
    }

    usuarios.append(usuario)

    proximo_id += 1

    return usuario

