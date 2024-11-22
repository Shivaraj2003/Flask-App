from app import app
from app.models import init_db

# Initialize the database (create tables)
with app.app_context():
    init_db()


if __name__ == "__main__":
    app.run(debug=True)
