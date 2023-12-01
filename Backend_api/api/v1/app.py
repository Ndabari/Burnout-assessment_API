#!/usr/bin/env python3
"""
    Route Module for the API
"""
from os import getenv

from Backend_api.api.v1.views import app_views
from flask import Flask, jsonify, abort, request, Response
from flask_cors import (CORS)
from Backend_api.api.v1.auth.auth import Auth

app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r'/api/v1/*': {'origins': '*'}})
auth = Auth()


@app.errorhandler(401)
def unauthorized_error(error) -> tuple[Response, int]:
    """
        Request Unauthorized handler
        :param error:
        :return: JSON{"error": "Unauthorized"}
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden_error(error) -> str:
    """
        Request Forbidden error handler
        :param error:
        :return: JSON{"error": "Forbidden"}
    """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(404)
def not_found(error) -> str:
    """
        Request Not found error handler
        :param error:
        :return: JSON{"error": "Unauthorized"}
    """
    return jsonify({"error": "Not Found"}), 404


@app.before_request
def before_request():
    """
        Executed before a request is handled
        :return:
    """
    ex_path = ['/api/v1/status/', '/api/v1/unauthorized/',
               '/api/v1/forbidden/', '/api/v1/auth/signin/', '/api/v1/auth/signup/', '/api/v1/burn-rate/get-questions/']

    if not auth.require_auth(request.path, ex_path):
        return
    elif auth.is_session_token_valid(request) is None:
        print(request.authorization)
        abort(401)
    elif auth.current_user(request) is None:
        abort(403)
    else:
        request.current_user = auth.current_user(request)


if __name__ == '__main__':
    host = getenv('API_HOST', '0.0.0.0')
    port = getenv('API_PORT', 5001)
    app.run(host=host, port=port, debug=True)
