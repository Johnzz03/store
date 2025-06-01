from db import db

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    payment_method = db.Column(db.String(20))
    ewallet_number = db.Column(db.String(20))
    cardname = db.Column(db.String(100))
    cardnumber = db.Column(db.String(20))
    expdate = db.Column(db.String(10))
    cvv = db.Column(db.String(10))
    total_price = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())