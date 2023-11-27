#!/usr/bin/env python3
"""
    Handles routes for all burn-rate calculations
"""
from models.questions import Questions
from flask import request, jsonify, abort
from api.v1.views import app_views
from utils.db_conn import session


@app_views.route('/burn-rate/get-questions', methods=['GET'], strict_slashes=False)
def get_questions():
    burn_rate_questions = session.query(Questions).all()
    if burn_rate_questions:
        D1, D2, D3, D4, D5, D6, D7, D8, D9, E1, E2, E3, E4, E5, E6, E7, E8, E9 = burn_rate_questions
        print(D1)
        return (D1, D2, D3, D4, D5, D6, D7, D8, D9, E1, E2, E3, E4, E5, E6, E7, E8, E9), 200
    else:
        return jsonify({'error': 'Fetch Error'}), 400
