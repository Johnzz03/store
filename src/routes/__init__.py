# src/routes/__init__.py
from flask import Blueprint

main = Blueprint('main', __name__)

from . import product_routes  # Import all route modules here
# Add more: from . import other_routes if needed