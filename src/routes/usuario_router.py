from flask import Blueprint
from controllers.usuario_controller import listar

# Criação do Blueprint
def create_usuario_router():
    usuarios = Blueprint("usuarios", __name__)

    # Rota para listar usuários
    @usuarios.route("/listar", methods=["GET"])
    def listar_usuarios():
        return listar()

    return usuarios
