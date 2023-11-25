#!/usr/bin/env python3
from sqlalchemy import Column, Integer, String
from utils.db_conn import Base, session


class Questions(Base):
    __tablename__ = 'questions'

    id = Column(Integer, primary_key=True)
    questions = Column(String)

    def __init__(self, question):
        self.question = question

    def get_all_questions(self):
        return session.query(Questions).all()

    def change_question(self, question_id, new_question):
        pass
