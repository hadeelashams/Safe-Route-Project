# backend/__init__.py
from flask import Blueprint

# Create a Blueprint for authentication-related routes
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# IMPORTANT: Import the modules that *define* the routes after the blueprint is created
# This ensures that the decorators are applied to auth_bp before it's used elsewhere
from .login import login_routes
from .signup import signup_routes
