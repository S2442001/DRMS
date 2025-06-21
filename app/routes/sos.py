# app/routes/sos.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import SOSRequest, db
from app.forms import CreateSOS


sos=Blueprint('sos', __name__)

@sos.route('/dashboard')
@login_required
def dashboard():
    if current_user.is_authenticated or current_user.role == 'user':
        sos_requests=SOSRequest.query.filter_by(user_id=current_user.id).all()
        return render_template('user_dashboard.html', sos_requests=sos_requests)
    else:
        flash('Access denied. Users only.')
        return redirect(url_for('admin.admin_dashboard'))


@sos.route('/sos/create', methods=['GET', 'POST'])
@login_required
def create_sos():

    if current_user.is_authenticated or current_user.role == 'user':
        form=CreateSOS()
        if form.validate_on_submit():
            location=form.location.data
            description=form.description.data
            sos=SOSRequest(user_id=current_user.id,location=location, description=description)
            db.session.add(sos)
            db.session.commit()
            flash('SOS submitted successfully.')
            return redirect(url_for('sos.dashboard'))
    
        return render_template('create_sos.html', form=form)
    flash('Access denied. Users only.')
    return redirect(url_for('admin.admin_dashboard'))



