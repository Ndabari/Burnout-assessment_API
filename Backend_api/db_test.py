#!/usr/bin/env python3
from Backend_api.models.questions import Questions
from Backend_api.utils import session

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
