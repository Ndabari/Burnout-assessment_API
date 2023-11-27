#!/usr/bin/env python3
from models.questions import Questions
from utils.db_conn import session

"""
allUsers = session.query(User).all()
for user in allUsers:
    print(user)
"""
response = {}
all_questions = session.query(Questions).all()
for query in all_questions:
    response[query.id] = query.questions

print(response)
