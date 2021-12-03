# models.py

from flask_login import UserMixin
from . import db
from sqlalchemy import Table, Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
    nickname = db.Column(db.String(100))
    type = db.Column(db.String(10))
    time_created = db.Column(DateTime(timezone=True), server_default=func.now())
    expiry = db.Column(DateTime(timezone=True))
    vms = relationship("VM", secondary = 'users_vms', back_populates="users")

class VM(UserMixin, db.Model):
    __tablename__ = 'vms'
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(100), unique=True)
    aws_id = db.Column(db.String(100), unique=True)
    users = relationship("User", secondary = 'users_vms', back_populates = "vms")

class User_VMs(UserMixin, db.Model):
    __tablename__ = 'users_vms'
    user_id = db.Column(ForeignKey('users.id'), primary_key=True)
    vm_id = db.Column(ForeignKey('vms.id'), primary_key=True)
