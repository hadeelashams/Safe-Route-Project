from flask import render_template, request, redirect, url_for, flash
from . import auth_bp
from models import User
from db import db

def signup_routes():
    @auth_bp.route('/signup', methods=['GET', 'POST'])
    def signup():
        if request.method == 'POST':
            name = request.form['fullname']
            email = request.form['email']
            username = request.form['username']
            password = request.form['password']
            confirm_password = request.form['confirm_password']
            role = request.form['role']

            if password != confirm_password:
                flash("Passwords do not match.", "danger")
                return render_template('signup.html')

            existing_user = User.query.filter((User.Username == username) | (User.Email == email)).first()
            if existing_user:
                flash("Username or email already exists.", "danger")
                return render_template('signup.html')

            new_user = User(
                name=name,
                Email=email,
                Username=username,
                Password=password,  # plain text (not secure)
                role=role
            )

            db.session.add(new_user)
            db.session.commit()

            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('auth.login'))

        # This will now handle the GET request for the signup page
        return render_template('signup.html')