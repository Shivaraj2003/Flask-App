from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

def init_db():
    """Initializes the database (creates tables)."""
    db.create_all()  # Create all tables defined by the models



def insert_user(username, email, password):
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()

def get_all_users():
    """Fetches all users from the database."""
    users = User.query.all()  # Fetch all users
    return users
