# main.py

from flask import Blueprint, render_template
from flask_login import login_required, current_user
from flask import Flask, render_template, request, redirect, url_for
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import and_, or_, not_
from sqlalchemy.sql import text

main = Blueprint('main', __name__)



@main.route('/')
def index():
    db.create_all()

    #if current_user.is_authenticated:
    #     courses = Course.query.filter(Course.users.any(id=current_user.id)).all()
    #     #courses = Course.query.filter_by(User.id==current_user.id).all()
    #     return render_template('courses.html', courses=courses, user=current_user)
    #else:
    return render_template("index.html")

@main.route('/machines')
@login_required
def machines():
    return render_template("machines.html")

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)
