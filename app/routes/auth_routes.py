from flask import Blueprint, current_app
from app.controllers.auth_controller import login, logout

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['GET', 'POST'])
def login_route():
    db = current_app.config['db_connection']
    return login(db)

@auth_bp.route('/logout')
def logout_route():
    return logout()

