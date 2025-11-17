import os
import json
from flask import jsonify, Response

@app.route('/swagger.json')
def swagger_json():
    try:
        path = os.path.join(app.static_folder, 'swagger.json')
        with open(path, 'r', encoding='utf-8') as f:
            data = f.read()

        json.loads(data)

        return Response(
            response=data,
            status=200,
            mimetype='application/json',
            headers={
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'GET, OPTIONS',
                'Access-Control-Allow-Headers': 'Content-Type, Authorization'
            }
        )

    except FileNotFoundError:
        return jsonify(error="swagger.json not found"), 404

    except json.JSONDecodeError as e:
        return jsonify(error="invalid swagger.json", detail=str(e)), 500

    except Exception as ex:
        return jsonify(error="unexpected error", detail=str(ex)), 500
