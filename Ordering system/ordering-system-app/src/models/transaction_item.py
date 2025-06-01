from db import db

class TransactionItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    transaction_id = db.Column(db.Integer, db.ForeignKey('transaction.id'))
    name = db.Column(db.String(100))
    price = db.Column(db.Float)
    image = db.Column(db.String(200))
    transaction = db.relationship('Transaction', backref='items')