from flask import request, redirect, render_template, session, url_for, flash
import psycopg2.extras

def login(db):
    if request.method == 'POST':
        email = request.form['email']
        contrasena = request.form['contrasena']

        with db.cursor(cursor_factory=psycopg2.extras.DictCursor) as cursor:
            cursor.execute("SELECT * FROM usuarios WHERE email = %s AND contrasena = %s", (email, contrasena))
            usuario = cursor.fetchone()

        if usuario:
            session['usuario'] = dict(usuario)  # Convertir a dict para guardar en session
            rol = usuario['id_rol']
            if rol == 1:
                return redirect(url_for('dashboard.dashboard_admin'))
            elif rol == 2:
                return redirect(url_for('dashboard.dashboard_medico'))
            elif rol == 4:
                return redirect(url_for('dashboard.dashboard_recepcionista'))
            else:
                flash("Rol no autorizado")
                return redirect(url_for('login'))
        else:
            flash('Credenciales incorrectas')
            return redirect(url_for('login'))

    return render_template('login.html')

def logout():
    session.clear()
    return redirect(url_for('auth.login_route'))
