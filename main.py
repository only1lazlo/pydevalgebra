#users
#posts
import os
import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

BASE_DIR= os.path.dirname(os.path.realpath(__file__))

conn = "sqlite:///"+os.path.join(BASE_DIR, 'blog.sqlite')


engine = create_engine(conn, echo=True)

Base = declarative_base()


##############################################################################
##############################################################################
# PRIMJER KAKO NAPRAVITI RELATIONSHIP POMOĆU BACKREF


# POSTOJI I DRUGI PRIMJER KAKO TO NAPRAVITI S back_populates
#  https://youtu.be/cc0xt9uuKQo?t=1617

##############################################################################
##############################################################################
"""
class User:
    id:int  pk
    username:str
    email:str


class Post:
    id:int  pk
    title:str
    content:str
    user_id:int foreign key
"""

class User(Base):
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(40), nullable= False)
    email = db.Column(db.String(80), nullable=False)
    posts= relationship("Post", backref='author', cascade='all, delete')

    def __repr__(self):
        return f"<User {self.username}>"
    
class Post(Base):
    __tablename__ ="posts"
    id = db.Column(db.Integer(), primary_key=True) 
    title=db.Column(db.String(45), nullable=False)
    content=db.Column(db.String(255), nullable=False)
    user_id= db.Column(db.Integer(), db.ForeignKey("users.id"))   

    def __repr__(self):
        return f"<User {self.title}>"
    

Base.metadata.create_all(engine)
session = sessionmaker()(bind=engine)