from application import db, bcrypt
from application import models

db.drop_all()
db.create_all()
hashed_pw = bcrypt.generate_password_hash('password')
user = models.Users(first_name='test_first_name', last_name='test_last_name', email='test@test.com', password=hashed_pw, admin=True)
user2 = models.Users(first_name='Ben', last_name='Hesketh', email='ben@ben.com', password=hashed_pw, admin=False)
db.session.add(user2)
db.session.add(user)
db.session.commit()