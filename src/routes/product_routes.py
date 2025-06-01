from . import main
from flask import render_template, request, redirect, url_for, session, flash
from models import Contact, Cart, db  # adjust import as needed
from models.transaction import Transaction
from models.transaction_item import TransactionItem
from models.product import Product  # make sure you have a Product model

@main.route('/')
def home():
    return render_template('base.html')

@main.route('/home2')
def home2():
    return render_template('home2.html')

@main.route('/products')
def products():
    return "Product List Page"

@main.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    name = request.form.get('name')
    price = request.form.get('price')
    image = request.form.get('image')  # Get image filename from form
    cart_item = Cart(product_id=product_id, name=name, price=price, image=image)
    db.session.add(cart_item)
    db.session.commit()
    return redirect(url_for('main.home2'))

@main.route('/add_to_cart_from_all/<int:product_id>', methods=['POST'])
def add_to_cart_from_all(product_id):
    product = Product.query.get_or_404(product_id)
    cart_item = Cart(
        product_id=product.id,
        name=product.name,
        price=product.price,
        image=product.image
    )
    db.session.add(cart_item)
    db.session.commit()
    return redirect(url_for('main.all_products'))

@main.route('/cart')
def view_cart():
    cart_items = Cart.query.all()
    return render_template('cart.html', cart_items=cart_items)

@main.route('/cart/edit/<int:cart_id>', methods=['GET', 'POST'])
def edit_cart_item(cart_id):
    cart_item = Cart.query.get_or_404(cart_id)
    if request.method == 'POST':
        cart_item.name = request.form.get('name')
        cart_item.price = request.form.get('price')
        db.session.commit()
        return redirect(url_for('main.view_cart'))
    return render_template('edit_cart_item.html', cart_item=cart_item)

@main.route('/cart/delete/<int:cart_id>', methods=['POST'])
def delete_cart_item(cart_id):
    cart_item = Cart.query.get_or_404(cart_id)
    db.session.delete(cart_item)
    db.session.commit()
    return redirect(url_for('main.view_cart'))

@main.route('/cart/buy_all', methods=['POST'])
def buy_all_cart():
    # Implement your buy logic here (e.g., clear the cart)
    Cart.query.delete()  # This deletes all items from the cart table
    db.session.commit()
    message = "All items purchased successfully!"
    cart_items = []
    return render_template('cart.html', cart_items=cart_items, message=message)

@main.route('/cart/pay_center', methods=['GET', 'POST'])
def pay_center():
    if request.method == 'POST':
        payment_method = request.form.get('payment_method')
        ewallet_number = request.form.get('ewallet_number')
        cardname = request.form.get('cardname')
        cardnumber = request.form.get('cardnumber')
        expdate = request.form.get('expdate')
        cvv = request.form.get('cvv')
        cart_items = Cart.query.all()
        total_price = sum(item.price for item in cart_items)
        transaction = Transaction(
            payment_method=payment_method,
            ewallet_number=ewallet_number,
            cardname=cardname,
            cardnumber=cardnumber,
            expdate=expdate,
            cvv=cvv,
            total_price=total_price  # <-- Save total price
        )
        db.session.add(transaction)
        db.session.commit()  # So transaction.id is available

        # Save all cart items as TransactionItems
        for item in cart_items:
            t_item = TransactionItem(
                transaction_id=transaction.id,
                name=item.name,
                price=item.price,
                image=item.image  # if you want to save images
            )
            db.session.add(t_item)

        # Clear the cart
        Cart.query.delete()
        db.session.commit()
        return render_template('thank_you.html')
    return render_template('pay_center.html')

@main.route('/sell', methods=['GET', 'POST'])
def sell_products():
    message = None
    error = None
    if request.method == 'POST':
        name = request.form.get('name')
        description = request.form.get('description')
        price = request.form.get('price')
        if not name or not description or not price:
            error = "All fields are required."
        else:
            try:
                product = Product(name=name, description=description, price=price)
                db.session.add(product)
                db.session.commit()
                message = "Product listed successfully!"
            except Exception as e:
                db.session.rollback()
                error = "Error saving product."
    return render_template('sell_products.html', message=message, error=error)

@main.route('/ordernow')
def order_now():
    return render_template('ordernow.html')

@main.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')

@main.route('/contact', methods=['GET', 'POST'])
def contact():
    success = None
    error = None
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        if name and email and message:
            new_contact = Contact(name=name, email=email, message=message)
            db.session.add(new_contact)
            db.session.commit()
            success = "Thank you for contacting us!"
        else:
            error = "Please fill in all fields."
    return render_template('contact.html', success=success, error=error)

@main.route('/admin/contacts')
def admin_contacts():
    contacts = Contact.query.order_by(Contact.id.desc()).all()
    return render_template('admin_contact.html', contacts=contacts)

@main.route('/edit_and_back/<int:cart_id>', methods=['GET', 'POST'])
def edit_and_back(cart_id):
    cart_item = Cart.query.get_or_404(cart_id)
    products = [
        {"name": "Headsets", "price": 49.99, "image": "headset.jpg"},
        {"name": "keyboard", "price": 39.99, "image": "keyboard.jpg"},
        {"name": "Mouse", "price": 19.99, "image": "mouse.jpg"},
        {"name": "cahair", "price": 89.99, "image": "chair.jpg"},
        {"name": "cleaning", "price": 29.99, "image": "cleaning.jpg"},
        {"name": "storage", "price": 39.99, "image": "storage.jpg"},
        {"name": "decor", "price": 59.99, "image": "decor.jpg"},
        {"name": "bedding", "price": 79.99, "image": "bedding.jpg"},
        {"name": "jeans", "price": 49.99, "image": "jeans.jpg"},
        {"name": "Dress", "price": 29.99, "image": "dress.jpg"},
        {"name": "Shoes", "price": 49.99, "image": "shoes.jpg"},
        {"name": "Tops", "price": 24.99, "image": "tops.jpg"}
        # ... your products list ...
    ]
    if request.method == 'POST':
        cart_item.name = request.form.get('name')
        cart_item.price = request.form.get('price')
        db.session.commit()
        # Redirect to cart after saving
        return redirect(url_for('main.view_cart'))
    return render_template('edit_cart_item.html', cart_item=cart_item, products=products)

@main.route('/transactions')
def view_transactions():
    transactions = Transaction.query.order_by(Transaction.timestamp.desc()).all()
    return render_template('transactions.html', transactions=transactions)

@main.route('/transaction/<int:transaction_id>')
def transaction_detail(transaction_id):
    transaction = Transaction.query.get_or_404(transaction_id)
    items = TransactionItem.query.filter_by(transaction_id=transaction_id).all()
    return render_template('transaction_detail.html', transaction=transaction, items=items)

@main.route('/transaction/delete/<int:transaction_id>', methods=['POST'])
def delete_transaction(transaction_id):
    transaction = Transaction.query.get_or_404(transaction_id)
    # Optionally delete related items
    TransactionItem.query.filter_by(transaction_id=transaction_id).delete()
    db.session.delete(transaction)
    db.session.commit()
    return redirect(url_for('main.view_transactions'))

@main.route('/all_products')
def all_products():
    products = Product.query.all()
    return render_template('all_products.html', products=products)