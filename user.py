from base_class import Base

class User(Base):
    __tablename__ = 'users'

    id = ('integer', 'not null')
    username = ('varchar(256)', 'not null')
    password = ('varchar(256)', 'not null')


user = User()
user.create()
#user.insert({'id': 20, 'username': 'alex', 'username_2': 'alex', 'password': 12345})
#user.insert({'id': 7, 'username': 'ivan'})
#user.insert({'id': 3, 'username': 'alex', 'password': 12345})
#user.select_all()
#user.update('username_2 = "misha"', 'id = 20')
#user.select_all()
#user.select('username', 'id < 5')
#user.select('id, username')
#user.delete()
