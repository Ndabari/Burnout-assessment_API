#!/usr/bin/env python3
"""
    User view module
"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.user import User
from utils.db_conn import session


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def view_all_users():
    """
        GET /api/v1/users
        :return: List of all user objects
    """
    all_users = [user.to_json() for user in session.query(User).all()]
    return jsonify(all_users)


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def view_one_users(user_id: str = None):
    """
        GET /api/v1/users/:id
        :return: user
    """
    if user_id is None or user_id == '':
        abort(404)
    else:
        user = session.query(User).filter_by(id=user_id).first()
        return jsonify(user.to_json())
