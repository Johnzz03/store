from flask import Blueprint, render_template, request, redirect, url_for, session

user_main = Blueprint('user_main', __name__)

@user_main.route('/users')
def users():
    # Placeholder for user listing
    return "User List Page"

@user_main.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        # Add authentication logic here
        # If login is successful:
        return redirect(url_for('main.home2'))
    return render_template('login.html', error=error)

@user_main.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        # Add registration logic here
        return redirect(url_for('user_main.login'))
    return render_template('register.html', error=error)

@user_main.route('/logout')
def logout():
    session.clear()  # Remove all session data (logs out the user)
    return redirect(url_for('main.home'))  # Redirect to login page