from application import db, bcrypt
from application import models

db.drop_all()
db.create_all()
hashed_pw = bcrypt.generate_password_hash('password')
user = models.Users(first_name='test_first_name', last_name='test_last_name', email='test@test.com', password=hashed_pw)
db.session.add(user)
db.session.commit()