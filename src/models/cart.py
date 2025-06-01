from db import db

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer)
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    image = db.Column(db.String(200))  # <-- Add this line