#!/usr/bin/env python3
from flask import Blueprint, request, jsonify
from Backend_api.models.user import User
bp_views = Blueprint('bp_views', __name__, url_prefix='/auth')


@bp_views.route('/signup', methods=['POST'], strict_slashes=False)
def signin():
    """
        POST /auth/login
        :return: session token
    """
    user_email = request.json.get('email')
    user_password = request.json.get('password')

    found_user = User.search({'email': user_email})
    print(found_user)

    if not found_user:
        return jsonify({'error': 'No user found for this email'}), 404
    else:
        for user in found_user:
            if user.is_valid_password(user_password):
                from Backend_api.api.v1.auth.token_auth import TokenAuth
                session_token = TokenAuth.create_token(user.id)
                response = jsonify(user.to_json())
                response.set_cookie('session-token', session_token)
                return response, 200
            else:
                return jsonify({'error': 'Wrong password'}), 401
