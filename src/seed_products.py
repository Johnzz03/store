from app import app, db
from models import Product

sample_products = [
    Product(name="Laptop", description="High performance laptop", price=999.99, seller_id=1),
    Product(name="Smartphone", description="Latest model smartphone", price=699.99, seller_id=1),
    Product(name="Headphones", description="Noise-cancelling headphones", price=199.99, seller_id=1),
    Product(name="Keyboard", description="Mechanical keyboard", price=89.99, seller_id=1),
    Product(name="Computer Mouse", description="Wireless mouse", price=49.99, seller_id=1),
    Product(name="Chair", description="Ergonomic office chair", price=149.99, seller_id=1),
    Product(name="Cleaning Tools", description="Set of cleaning tools", price=29.99, seller_id=1),
    Product(name="Home Storage", description="Storage boxes", price=39.99, seller_id=1),
    Product(name="Home Decor", description="Modern home decor", price=59.99, seller_id=1),
    Product(name="Bedding", description="Comfortable bedding set", price=79.99, seller_id=1),
    Product(name="Jeans", description="Jeans under $50", price=49.99, seller_id=1),
    Product(name="Tops", description="Tops under $25", price=24.99, seller_id=1),
    Product(name="Dress", description="Dress under $30", price=29.99, seller_id=1),
    Product(name="Shoes", description="Shoes under $50", price=49.99, seller_id=1),
]

with app.app_context():
    db.session.bulk_save_objects(sample_products)
    db.session.commit()
    print("Sample products added to the database.")