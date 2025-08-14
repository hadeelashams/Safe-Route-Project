# backend/login.py
from flask import render_template, request, redirect, url_for, flash
from . import auth_bp  # Import the blueprint
from models import User
from db import db # You might need db here for querying

# We define a function, which registers the routes with the blueprint
def login_routes():
    @auth_bp.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']

            user = User.query.filter_by(Username=username).first()

            if user and user.Password == password: # Direct comparison (WARNING: HIGH SECURITY RISK)
                flash('Login successful!', 'success')
                # Redirect based on role
                if user.role == 'admin':
                    return redirect(url_for('admin_dashboard'))
                elif user.role == 'user':
                    return redirect(url_for('dashboard'))
                else:
                    flash('Unknown user role.', 'danger')
                    return render_template('login.html')
            else:
                flash('Invalid username or password', 'danger')

        return render_template('login.html')

    # You could also add other login-related routes here if needed
    # @auth_bp.route('/logout')
    # def logout():
    #     # ... logout logic ...
    #     flash('Logged out successfully.', 'info')
    #     return redirect(url_for('auth.login')) # Redirect to login after logout
