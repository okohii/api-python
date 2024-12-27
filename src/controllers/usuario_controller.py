from flask import jsonify, Response, Request
from models.usuario_model import listar as listar_model

def listar():
  
    try:
        resultado = listar_model()
        if len(resultado) < 1:
            print("Nenhuma informação encontrada.")
            return Response(status=204)
        else:
            return jsonify(resultado)

    except Exception as erro:
        print(erro)
        return jsonify({"erro": str(erro)}), 500