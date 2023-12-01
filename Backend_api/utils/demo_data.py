from Backend_api.models.user import User
from Backend_api.utils.db_conn import Base, session, engine

Base.metadata.create_all(engine)

# demo users
user_1 = User('Thomas', 'Okoyo', 'okoyotommy@gmail.com', 'password', 'admin')
user_2 = User('Sera', 'Ndabari', 'ndabarisera@gmail.com', 'password', 'admin')
user_3 = User('Robert', 'Okoyo', 'okoyorobert@gmail.com', 'password', 'user')
user_4 = User('Maryanne', 'Atieno', 'atieno@gmail.com', 'password', 'user')
user_5 = User('Jesse', 'Juma', 'jessejuma@gmail.com', 'password', 'user')
user_6 = User('Naomi', 'Ndabari', 'naomi@gmail.com', 'password', 'user')

session.add(user_1)
session.add(user_2)
session.add(user_3)
session.add(user_4)
session.add(user_5)
session.add(user_6)

session.commit()
session.close()
