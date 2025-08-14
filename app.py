# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from db import db
from models import User, Destination
import os

# Blueprints for auth
from backend import auth_bp
from backend.login import login_routes
from backend.signup import signup_routes

app = Flask(__name__)

# -------------------
# Configuration
# -------------------
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/saferouteai'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(24)

db.init_app(app)

with app.app_context():
    db.create_all()

# -------------------
# Auth Blueprints
# -------------------
login_routes()
signup_routes()
app.register_blueprint(auth_bp)

# -------------------
# Routes
# -------------------

# Landing Page
@app.route('/')
def landing():
    return render_template('landing.html')

# User Dashboard
@app.route('/dashboard')
def dashboard():
    return render_template('user_dashboard.html')

# Admin main page (with sidebar)
@app.route('/admin/content')
def admin_dashboard():
    total_users = User.query.count()
    total_destinations = Destination.query.count()
    top_search = Destination.query.first()
    return render_template(
        'admin_dashboard.html',
        total_users=total_users,
        total_destinations=total_destinations,
        top_search_name=top_search.Name if top_search else "N/A"
    )

# -------------------
# Manage Destinations
# -------------------

@app.route('/admin/manage_destinations')
def manage_destinations():
    destinations = Destination.query.all()
    return render_template('manage_destination.html', destinations=destinations)

@app.route('/admin/add-destination', methods=['POST'])
def add_destination():
    data = request.get_json()
    name = data.get('name')
    safety = data.get('safety')
    description = data.get('description')

    if not name or not safety or not description:
        return jsonify({'success': False, 'message': 'All fields are required'}), 400

    new_dest = Destination(Name=name, Safety=safety, Description=description)
    db.session.add(new_dest)
    db.session.commit()

    return jsonify({
        'success': True,
        'destination': {
            'id': new_dest.id,
            'name': new_dest.Name,
            'safety': new_dest.Safety,
            'description': new_dest.Description
        }
    })

@app.route('/admin/delete-destination/<int:dest_id>', methods=['POST'])
def delete_destination(dest_id):
    dest = Destination.query.get_or_404(dest_id)
    db.session.delete(dest)
    db.session.commit()
    return jsonify({'success': True})

@app.route('/admin/edit-destination/<int:dest_id>', methods=['POST'])
def edit_destination(dest_id):
    dest = Destination.query.get_or_404(dest_id)
    data = request.get_json()
    dest.Name = data.get('name', dest.Name)
    dest.Safety = data.get('safety', dest.Safety)
    dest.Description = data.get('description', dest.Description)
    db.session.commit()
    return jsonify({'success': True})

# -------------------
# Manage Users
# -------------------
@app.route('/admin/manage_users')
def manage_users():
    users = User.query.all()
    return render_template('manage_users.html', users=users)

# -------------------
# Run Server
# -------------------
if __name__ == '__main__':
    app.run(debug=True)
