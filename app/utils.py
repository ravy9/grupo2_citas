from functools import wraps
from flask import session, redirect, url_for

def login_required(rol_requerido=None):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            usuario = session.get('usuario')
            if not usuario:
                return redirect(url_for('auth.login_route'))
            if rol_requerido and usuario['id_rol'] != rol_requerido:
                return redirect(url_for('auth.login_route'))  # o una página de acceso denegado
            return f(*args, **kwargs)
        return decorated_function
    return decorator
