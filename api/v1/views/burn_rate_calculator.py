#!/usr/bin/env python3
"""
    Handles routes for all burn-rate calculations
"""
from models.questions import Questions
from models.scores import Scores
from flask import request, jsonify, abort
from api.v1.views import app_views
from utils.burn_rate_calc import BurnoutCalculator
from utils.db_conn import session


@app_views.route('/burn-rate/get-questions', methods=['GET'], strict_slashes=False)
def get_questions():
    response = {}
    burn_rate_questions = session.query(Questions).all()
    if burn_rate_questions:
        for question in burn_rate_questions:
            response[question.id] = question.questions
        return jsonify(response), 200
    else:
        return jsonify({'error': 'Fetch Error'}), 400


@app_views.route('/burn-rate/get-score', methods=['POST'], strict_slashes=False)
def get_burnout_score():
    D1 = request.json.get('D1')
    D2 = request.json.get('D2')
    D3 = request.json.get('D3')
    D4 = request.json.get('D4')
    D5 = request.json.get('D5')
    D6 = request.json.get('D6')
    D7 = request.json.get('D7')
    D8 = request.json.get('D8')
    D9 = request.json.get('D9')
    E1 = request.json.get('E1')
    E2 = request.json.get('E2')
    E3 = request.json.get('E3')
    E4 = request.json.get('E4')
    E5 = request.json.get('E5')
    E6 = request.json.get('E6')
    E7 = request.json.get('E7')
    E8 = request.json.get('E8')
    E9 = request.json.get('E9')
    user_id = request.current_user

    if not (D1 or D2 and D3 or D4) and (D5 or D6 and D7 or (D8 or D9)):
        return jsonify({'error': 'Missing Values D'}), 400
    elif not (E1 or E2 and E3 or E4) and (E5 or E6 and E7 or (E8 or E9)):
        return jsonify({'error': 'Missing Values E'}), 400
    elif not user_id:
        return jsonify({'error': 'Internal Error (user)'}), 400
    else:
        Exhaustion_scores = [int(E1), int(E2), int(E3), int(E4), int(E5), int(E6), int(E7), int(E8), int(E9)]
        Disengagement_score = [int(D1), int(D2), int(D3), int(D4), int(D5), int(D6), int(D7), int(D8), int(D9)]
        Burn_rate = BurnoutCalculator.burnout_calculator(Disengagement_score, Exhaustion_scores)

        if session.query(Scores).filter_by(user_id=user_id).first():
            pass
        else:
            pass
        response = {
            'Total Score': Burn_rate.get('score'),
            'Burnout Level': Burn_rate.get('burnout_level')
        }

        return jsonify(response), 200

