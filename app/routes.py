from flask import Blueprint, render_template, request, redirect, url_for
from app.models import insert_user, get_all_users


# Create a Blueprint for routes
app_routes = Blueprint('app_routes', __name__)

@app_routes.route('/')
def index():
    return render_template('index.html')

@app_routes.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')


        # Insert user into the database
        insert_user(username, email, password)
        
        return redirect(url_for('app_routes.view'))

    return render_template('signup.html')


@app_routes.route('/view_db')
def view():
    # Fetch all users from the database
    users = get_all_users()
    
    # Render the success page and pass the list of users
    return render_template('success.html', users=users)
