#!/usr/bin/env python3
from sqlalchemy import Column, String
from Backend_api.utils.db_conn import Base, session


class Questions(Base):
    __tablename__ = 'questions'

    id = Column(String(40), primary_key=True)
    questions = Column(String(500))

    def __init__(self, q_id, question):
        self.id = q_id
        self.questions = question

    def __str__(self):
        return f'{self.id}, {self.questions}'

    def get_all_questions(self):
        return session.query(Questions).all()

    def change_question(self, question_id, new_question):
        pass

    def to_dict(self) -> dict:
        """
            Convert the objects to a dict
            :return: dict object
        """
        return {
            'question_id': self.id,
            'question': self.questions
        }
