from base_class import Base

class Post(Base):
    __tablename__ = 'posts'

    id = ('integer', 'not null')
    title = ('varchar(256)', 'not null')
    post = ('text', 'not null')
    user_id = ('integer', 'null', {'users': 'posts.user_id = users.id'})

post = Post()
post.create()
post.insert({'id': 1, 'title': 'test', 'post': 'alex', 'user_id': 20})
post.select('title,post')
