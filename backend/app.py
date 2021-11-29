from flask import Flask, request, jsonify, abort, make_response
from flask_cors import CORS
from ahorcado.ahorcado import Ahorcado

app = Flask(__name__)
CORS(app)
ahorcado = Ahorcado()

class APIError(Exception):
    """All custom API Exceptions"""
    pass

class InvalidInputError(APIError):
    """Custom invalid input error class."""
    code = 402
    description = "Invalid input"

@app.errorhandler(APIError)
def handle_exception(err):
    """Return custom JSON when APIError or its children are raised"""
    response = {"error": err.description, "message": ""}
    if len(err.args) > 0:
        response["message"] = err.args[0]
    # Add some logging so that we can monitor different types of errors
    app.logger.error(f'{err.description}: {response["message"]}')
    return jsonify(response), err.code

@app.errorhandler(500)
def handle_exception(err):
    """Return JSON instead of HTML for any other server error"""
    app.logger.error(f"Unknown Exception: {str(err)}")
    app.logger.debug(''.join(traceback.format_exception(etype=type(err), value=err, tb=err.__traceback__)))
    response = {"error": "Sorry, that error is on us, please contact support if this wasn't an accident"}
    return jsonify(response), 500


@app.route('/login', methods=['POST'])
def login():
    nombre = request.get_json()['name']
    try:
        ahorcado.login(nombre)
    except Exception as error:
        raise InvalidInputError(str(error))

    return jsonify(ahorcado.get_nombre()), 200

@app.route('/initialize', methods=['POST'])
def initialize():
    word_to_guess = request.get_json()['wordToGuess']
    ahorcado.inicializar_partida()
    try:
        ahorcado.set_palabra(word_to_guess)
    except Exception as error:
        raise InvalidInputError(str(error))

    return jsonify(word_to_guess), 200

@app.route('/get_state', methods=['GET'])
def get_state():
    estado = ahorcado.get_estado()
    aciertos, errores = ahorcado.get_aciertos_errores()
    codigo_estado = ahorcado.get_codigo_estado()
    partida = {
        'estado': estado,
        'aciertos': aciertos,
        'errores': errores,
        'codigoEstado': codigo_estado,
        'progreso': 100*aciertos/len(ahorcado.get_palabra())
    }
    return jsonify(partida), 200

@app.route('/arriesgar', methods=['POST'])
def arriesgar():
    user_input = request.get_json()['userInput']
    if len(user_input) > 1:
        res = ahorcado.arriesgar_una_palabra(user_input)
    else:
        res = ahorcado.arriesgar_una_letra(user_input)
    return get_state()
