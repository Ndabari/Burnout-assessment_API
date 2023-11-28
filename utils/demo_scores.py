from models.scores import Scores
from models.user import User
from utils.db_conn import Base, session, engine

Base.metadata.create_all(engine)

user = 'a8ecade8-461b-472b-8c80-20110f759a8a'
user_obj = session.query(User).filter_by(id=user).first()


score_1 = Scores(user, 45)

session.commit(score_1)
session.close()
