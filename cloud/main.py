# main.py

from flask import Blueprint, render_template, flash
from flask_login import login_required, current_user
from flask import Flask, render_template, request, redirect, url_for
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import and_, or_, not_
from sqlalchemy.sql import text
from .models import VM

main = Blueprint('main', __name__)

import boto3

awsclient = boto3.client('ec2', region_name='eu-central-1')

@main.route('/')
def index():
    db.create_all()

    if current_user.is_authenticated:
        return redirect(url_for('main.machines'))

    return render_template("index.html")

@main.route('/machines')
@login_required
def machines():
    vms = VM.query.filter(VM.users.any(id=current_user.id)).all()
    vmnew = []
    for vm in vms:
        # check status of VM
        ec2_resource = boto3.resource('ec2', region_name='eu-central-1')
        instance = ec2_resource.Instance(vm.aws_id)
        state=instance.state['Name']

        vmnew.append({'name': vm.name,
                       'state': state,
                       'id': vm.id}
                       )
    return render_template("machines.html", vms = vmnew)


@main.route('/modifyvm/<vm_id>/<status>')
def modifyvm(vm_id, status):
    # verify whether user has rights to change status
    vm = VM.query.filter(VM.id==vm_id).filter(VM.users.any(id=current_user.id)).first()

    if not vm:
        flash('Cannot change status.')
    flash(vm.aws_id)
    if vm:
        if (status=='start'): instance = awsclient.start_instances(InstanceIds=[vm.aws_id])
        if (status=='stop'): instance = awsclient.stop_instances(InstanceIds=[vm.aws_id])
    return redirect(url_for('main.machines'))


@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
