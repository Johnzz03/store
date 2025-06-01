from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from models.chat_message import ChatMessage
from db import db

chat_main = Blueprint('chat_main', __name__)

@chat_main.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        username = request.form.get('username', 'Customer')
        message = request.form.get('message')
        if message:
            chat_msg = ChatMessage(username=username, message=message)
            db.session.add(chat_msg)
            db.session.commit()
        return redirect(url_for('chat_main.chat'))
    chat_history = ChatMessage.query.order_by(ChatMessage.timestamp.asc()).all()
    return render_template('chat.html', chat_history=chat_history)

@chat_main.route('/chat/messages')
def chat_messages():
    messages = ChatMessage.query.order_by(ChatMessage.timestamp.asc()).all()
    return jsonify([
        {'username': m.username, 'message': m.message, 'timestamp': m.timestamp.strftime('%Y-%m-%d %H:%M:%S')}
        for m in messages
    ])