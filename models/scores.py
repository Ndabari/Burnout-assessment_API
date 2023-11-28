#!/usr/bin/env python3
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from utils.db_conn import Base, session


class Scores(Base):
    __tablename__ = 'scores'

    user_id = Column(String, ForeignKey('users.id'))
    user = relationship('User', backref='scores')
    score = Column(Integer, primary_key=True)

    def __init__(self, user, score):
        self.user = user
        self.score = score

    def get_score(self):
        pass
