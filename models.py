from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    items = db.Column(db.Integer, nullable=False)
    delivery_date = db.Column(db.String(50), nullable=False)
    sender = db.Column(db.String(100), nullable=False)
    recipient = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(50), default="Ongoing")

class ActionLog(db.Model):
    __tablename__ = 'action_log'
    id = db.Column(db.Integer, primary_key=True)
    action = db.Column(db.String(50), nullable=False)
    performed_by = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
