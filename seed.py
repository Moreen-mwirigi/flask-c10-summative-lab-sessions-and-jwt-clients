from app import create_app
from extensions import db
from models import User, Note
from faker import Faker

fake = Faker()
app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    # Create a test user
    user1 = User(username='user1', email='user1@example.com', password='password1')
    user1.set_password = 'password1'
    db.session.add(user1)
    db.session.commit()

    for _ in range(5):
        note = Note(
            title=fake.sentence(),
            content=fake.text(),
            user_id=user1.id
        )
        db.session.add(note)
    db.session.commit()
    print("Database seeded with test user and notes.")