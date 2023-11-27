#!/usr/bin/env python3
from sqlalchemy import Column, Integer, String
from utils.db_conn import Base, session


class Questions(Base):
    __tablename__ = 'questions'

    id = Column(String(40), primary_key=True)
    questions = Column(String(500))

    def __init__(self, q_id, question):
        self.id = q_id
        self.questions = question

    def get_all_questions(self):
        return session.query(Questions).all()

    def change_question(self, question_id, new_question):
        pass

    def to_json(self, for_serialization: bool = False) -> dict:
        """
            Convert the object to a JSON dictionary
            :param for_serialization:
            :return: Dict
        """
        result = {}

        for key, value in self.__dict__.items():
            if not for_serialization and key[0] == '_':
                continue
            else:
                result[key] = value

        return result
