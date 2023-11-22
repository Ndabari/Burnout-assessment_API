#!/usr/bin/env python3
"""
    Session Authentication Module
"""
from models.user import User


class SessionAuth(Auth):
    """
        Responsible for session authorization and validation
        inherits from auth class
    """