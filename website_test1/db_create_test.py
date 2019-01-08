#coding:utf-8

"""
----------------------------------------
description:

author: sss

date:
----------------------------------------
change:
    
----------------------------------------

"""

__author__ = 'sss'

from flask_website.app import db
from flask_website.app import User, Movie

# db create
RUN = 1
if RUN:
    from flask_website.app import db,app
    #print(app.root_path)
    db.create_all()




# db test
# 添加记录测试
RUN = 0
if RUN:
    from flask_website.app import User, Movie  # 导入user = User(name='Grey Li')
    # 创建一个 User 记录
    user = User(name='Grey Li')  # 创建一个 User 记录
    m1 = Movie(title='Leon', year='1994')  # 创建一个 Movie 记录
    m2 = Movie(title='Mahjong', year='1996')  # 再创建一个 Movie 记录
    db.session.add(user)  # 把新创建的记录添加到数据库会话
    db.session.add(m1)
    db.session.add(m2)
    db.session.commit()


# 添加虚拟数据
RUN = 0
if RUN:
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]

    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)

    db.session.commit()

# 输出数据
RUN = 0
if RUN:
    from flask_website.app import Movie
    movie = Movie.query.all()
    for _ in movie:
       print(_.title)

