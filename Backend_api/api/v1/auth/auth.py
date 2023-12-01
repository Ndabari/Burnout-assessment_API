#!/usr/bin/env python3
"""
    This class manages the API authentication
"""
from typing import List
from Backend_api.api.v1.auth.token_auth import TokenAuth
token_auth = TokenAuth()

class Auth:
    """
        Authentication Class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
            Defines the routes that don't need authentication
            :param path: request path
            :param excluded_paths:
            :return:
        """
        if path is None or excluded_paths is None:
            return True
        elif path[-1] is '/':
            if path in excluded_paths:
                return False
        else:
            path += '/'
            if path in excluded_paths:
                return False

        return True

    def is_session_token_valid(self, request=None) -> str:
        """
            Gets the cookie value from the request
            :param request:
            :return:
        """
        if request is not None:
            session_token = request.cookies.get('session-token')
            if session_token:
                if token_auth.is_token_valid(session_token):
                    return False
                else:
                    return None
            else:
                return None
        else:
            return None

    def current_user(self, request=None):
        user_id = token_auth.decode_token(request.cookies.get('session-token')).get('User')
        if user_id:
            return user_id
        else:
            return None
