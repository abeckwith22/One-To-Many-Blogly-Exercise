"""Seed file to make sample data for users db."""
from models import User, Post, db
from app import app

app.app_context().push()

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it 
User.query.delete()

# Add users
QuantumQuasar23 = User(first_name='Alan', last_name='Alda')
VelvetVortex56 = User(first_name='Joel', last_name='Burton')
NimbusNebula77 = User(first_name='Jane', last_name='Smith')

# Adding users to db
db.session.add(QuantumQuasar23)
db.session.add(VelvetVortex56)
db.session.add(NimbusNebula77)

# commiting users to db before posts
db.session.commit()

# Adding posts
# NOTE: Formatting for created_at column is 'created_at("YYYY-MM-DD HH:MM:SS")'

# Quantum
p1 = Post(title="AITA for blowing up my neighbors car?",
          content="Lorem Ipsum", 
          created_at=('2020-05-03 08:29:12'), 
          user_id=1)
p2 = Post(title="Do you love birds as much as I do",                 
          content="Lorem Ipsum", 
          created_at=('2020-04-06 20:01:17'), 
          user_id=1)
# Velvet 
p3 = Post(title="Check out this cool underground hospital I found!", 
          content="Lorem Ipsum", 
          created_at=('2020-06-22 05:47:33'), 
          user_id=2)
p4 = Post(title="Who would win?",                                    
          content="Lorem Ipsum", 
          created_at=('2020-04-06 03:35:01'), 
          user_id=2)
# Nimbus
p5 = Post(title="Why is everyone so mean to me?",                    
          content="Lorem Ipsum", 
          created_at=('2020-12-06 23:59:22'), 
          user_id=3)
p6 = Post(title="I love creating sql models in python",               
          content="Lorem Ipsum", 
          created_at=('2020-04-06 12:29:10'), 
          user_id=3)

posts = [p1, p2, p3, p4, p5, p6] # didn't want to write 6 different db.session.add(pX)

db.session.add_all(posts)

#  Commiting posts to db
db.session.commit()
