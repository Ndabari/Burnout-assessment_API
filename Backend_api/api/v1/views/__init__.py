#!/usr/bin/env python3
"""
    View Module
"""
from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix='/api/v1')

from Backend_api.api.v1.views.index import *
