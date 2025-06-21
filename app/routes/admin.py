# app/routes/admin.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import SOSRequest, Shelter, Resource, db
from app.forms import ManageResource, ShelterForm

admin = Blueprint('admin', __name__)

@admin.route('/admin')
@login_required
def admin_dashboard():
    if current_user.role != 'admin':
        flash('Access denied. Admins only.')
        return redirect(url_for('sos.dashboard'))

    sos_requests = SOSRequest.query.all()
    return render_template('admin_dashboard.html', sos_requests=sos_requests)

@admin.route('/admin/resources', methods=['GET', 'POST'])
@login_required
def manage_resources():
    if current_user.role != 'admin':
        flash('Access denied. Admins only.')
        return redirect(url_for('sos.dashboard'))

    form=ManageResource()
    if form.validate_on_submit():
        rtype = form.type.data
        quantity = form.quantity.data
        location = form.location.data
        resource = Resource(type=rtype, quantity=quantity, location=location)
        db.session.add(resource)
        db.session.commit()
        flash('Resource added successfully.')
        return redirect(url_for('admin.manage_resources'))

    resources = Resource.query.all()
    return render_template('resources.html', resources=resources, form=form)


@admin.route('/admin/shelters', methods=['GET', 'POST'])
@login_required
def manage_shelters():
    if current_user.role != 'admin':
        flash('Access denied. Admins only.')
        return redirect(url_for('sos.dashboard'))

    form=ShelterForm()
    if form.validate_on_submit():
        name = form.name.data
        capacity =form.capacity.data
        available = form.available_beds.data
        location = form.location.data
        shelter = Shelter(name=name, capacity=capacity, available_beds=available, location=location)
        db.session.add(shelter)
        db.session.commit()
        flash('Shelter added successfully.')
        return redirect(url_for('admin.manage_shelters'))

    shelters = Shelter.query.all()
    return render_template('shelters.html', shelters=shelters, form=form)

@admin.route('/admin/update_status/<int:request_id>', methods=['POST'])
@login_required
def update_request_status(request_id):
    if current_user.role != 'admin':
        flash('Access denied. Admins only.')
        return redirect(url_for('sos.dashboard'))
    new_status = request.form.get('status')  # resolved or rejected
    sos_request = SOSRequest.query.get_or_404(request_id)
    
    if sos_request.status == 'Pending' and new_status in ['resolved', 'rejected']:
        sos_request.status = new_status
        db.session.commit()
        flash(f"SOS Request {request_id} marked as {new_status}.")
    else:
        flash("Invalid status update.")
    
    return redirect(url_for('admin.admin_dashboard'))