import os
from flask import Flask, jsonify, request, Response
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_cors import CORS

app = Flask(__name__, static_folder='static')
CORS(app)

app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'dev_secret_key')
jwt = JWTManager(app)

# ---- Handlers do JWT para mensagens claras ----
@jwt.unauthorized_loader
def missing_token_callback(err_str):
    return jsonify({"msg": "Missing Authorization Header", "error": err_str}), 401

@jwt.invalid_token_loader
def invalid_token_callback(err_str):
    return jsonify({"msg": "Invalid token", "error": err_str}), 422

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"msg": "Token has expired"}), 401

# ---- Rotas da API ----
@app.route('/')
def home():
    return jsonify(message="API is running")

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items=["item1", "item2", "item3"])

@app.route('/login', methods=['POST'])
def login():
    access_token = create_access_token(identity="user")
    return jsonify(access_token=access_token)

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(message="Protected route")

@app.route('/docs')
def swagger_ui():
    html = """
    <!doctype html>
    <html>
      <head>
        <meta charset="utf-8"/>
        <title>Swagger UI</title>
        <link rel="stylesheet" href="https://unpkg.com/swagger-ui-dist@4/swagger-ui.css"/>
      </head>
      <body>
        <div id="swagger-ui"></div>
        <script src="https://unpkg.com/swagger-ui-dist@4/swagger-ui-bundle.js"></script>
        <script src="https://unpkg.com/swagger-ui-dist@4/swagger-ui-standalone-preset.js"></script>
        <script>
        window.onload = function() {
          const ui = SwaggerUIBundle({
            url: "/static/swagger.json",
            dom_id: '#swagger-ui',
            presets: [SwaggerUIBundle.presets.apis, SwaggerUIStandalonePreset],
            layout: "StandaloneLayout",
            docExpansion: "none"
          })
          window.ui = ui
        }
        </script>
      </body>
    </html>
    """
    return Response(html, mimetype='text/html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 1313))
    app.run(host='0.0.0.0', port=port)
