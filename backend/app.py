from flask import app, Flask, make_response, request
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def index():
    resposta = make_response(
        jsonify(
            {
                'Status': '200'
            }
        )
    )
    resposta.headers['Access-Control-Allow-Origin'] = '*'
    return resposta


if __name__ == "__main__":
    app.run(host='localhost')
