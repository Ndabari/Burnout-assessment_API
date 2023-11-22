#!/usr/bin/env python3
from models.user import User
from utils.db_conn import session

allUsers = session.query(User).all()
for user in allUsers:
    print(user)
