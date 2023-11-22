#!/usr/bin/env python3
"""
    User module test
"""
from models.user import User

# create a sample test user
firstname = 'Thomas'
lastname = 'Okoyo'
user_email = 'okoyotommy@gmail.com'
user_password = 'password'
user = User()
user.firstname = firstname
user.lastname = lastname
user.email = user_email
user.password = user_password
print("New user: {} / {}".format(user.id, user.display_name()))
user.save()
