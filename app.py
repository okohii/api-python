from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import sys
import os

src_path = os.path.join(os.path.dirname(__file__), "src")
sys.path.append(src_path)

from routes.usuario_router import create_usuario_router



load_dotenv()

app = Flask(__name__)
CORS(app)

app.register_blueprint(create_usuario_router(), url_prefix="/usuarios")

if __name__ == "__main__":
    PORTA_APP = int(os.getenv("APP_PORT", 8080))
    HOST_APP = os.getenv("APP_HOST", "localhost")

    print(f"Servidor rodando em http://{HOST_APP}:{PORTA_APP}")
    app.run(host=HOST_APP, port=PORTA_APP, debug=True)
