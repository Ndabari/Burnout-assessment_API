#!/usr/bin/env python3
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref
from utils.db_conn import Base, session


class Responses(Base):
    __tablename__ = 'responses'

    user_id = Column(String, ForeignKey('users.id'))
    student = relationship('User', backref=backref('responses'))
    question_id = Column(Integer, ForeignKey('questions.id'))
    question = relationship('Questions', backref='responses')
    response = Column(Integer)

    def __init__(self, student, question, response):
        self. student = student
        self.question = question
        self.response = response

    def get_responses(self, user):
        """
            Gets responses of a particular user
            :param user:
            :return:
        """
        return session.query(Responses).filter_by(user_id=user.id).all()
