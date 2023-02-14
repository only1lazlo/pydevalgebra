from main import session, User, Post

user_to_delete = session.query(User).filter(User.id==1).first()

all_posts=session.query(Post).all()

all_users=session.query(User).all()

session.delete(user_to_delete)
session.commit()


print(all_posts)
print(all_users)