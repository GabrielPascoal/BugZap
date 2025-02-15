# site com os scripts: https://cdnjs.com/
# Framework (é um conjuto de ferramentas) -> Flask -> criar site
# jquery -> javascript
# Passo a Passo
# Passo 1 - Importação do flask
from flask import Flask, render_template
from flask_socketio import SocketIO, send
# Passo 2 - Criação do site ou app
# __name__ é uma variável privada do python, é o nome do arquivo que está executando
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# funcionalidade de enviar mensagem
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)

# Passo 3 - criar a 1° página = 1° rota - portalhashtag.com/>aulas<
@app.route("/")
def homepage():
    return render_template("index.html")


# roda o aplicativo
socketio.run(app, host="192.168.0.221")

#websocket é um túnel de comunicação entre dois ou mais computadores diferentes (tubo de conexão)