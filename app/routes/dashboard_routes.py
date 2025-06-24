from flask import Blueprint, render_template, session
from app.utils import login_required

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/dashboard_admin')
@login_required(rol_requerido=1)
def dashboard_admin():
    return render_template('dashboard_admin.html')

@dashboard_bp.route('/dashboard_medico')
@login_required(rol_requerido=2)
def dashboard_medico():
    return render_template('dashboard_medico.html')

@dashboard_bp.route('/dashboard_recepcionista')
@login_required(rol_requerido=4)
def dashboard_recepcionista():
    return render_template('dashboard_recepcionista.html')
