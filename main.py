from flask import Flask, jsonify
import modules

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
    return jsonify({"status": "ok", "data":
        {"description": "This is not an endpoint. Please use /rank or /match endpoints. Detailed information can be "
                        "found at https://github.com/ayberkenis/valorant-api"}})

for bp in modules.__all__:
    app.register_blueprint(getattr(modules, bp).bp)


def create_app():
    return app
