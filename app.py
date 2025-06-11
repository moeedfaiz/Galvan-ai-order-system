from flask import Flask, render_template, request, redirect, url_for
from models import db, Order, ActionLog
from datetime import datetime

app = Flask(__name__)
# Replace username, password, host, port, and db name as needed
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/orders_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

def log_action(action, performed_by):
    log = ActionLog(action=action, performed_by=performed_by)
    db.session.add(log)
    db.session.commit()

@app.route('/')
def index():
    orders = Order.query.all()
    return render_template('index.html', orders=orders)

@app.route('/add', methods=['GET', 'POST'])
def add_order():
    if request.method == 'POST':
        order = Order(
            items=int(request.form['items']),
            delivery_date=request.form['delivery_date'],
            sender=request.form['sender'],
            recipient=request.form['recipient'],
            address=request.form['address']
        )
        db.session.add(order)
        db.session.commit()
        log_action("Created", order.sender)
        return redirect(url_for('index'))
    return render_template('add_order.html')

@app.route('/edit/<int:order_id>', methods=['GET', 'POST'])
def edit_order(order_id):
    order = Order.query.get_or_404(order_id)
    if request.method == 'POST':
        order.items = int(request.form['items'])
        order.delivery_date = request.form['delivery_date']
        order.sender = request.form['sender']
        order.recipient = request.form['recipient']
        order.address = request.form['address']
        db.session.commit()
        log_action("Edited", order.sender)
        return redirect(url_for('index'))
    return render_template('edit_order.html', order=order)

@app.route('/deliver/<int:order_id>')
def deliver_order(order_id):
    order = Order.query.get_or_404(order_id)
    order.status = "Delivered"
    db.session.commit()
    log_action("Marked Delivered", order.sender)
    return redirect(url_for('index'))

@app.route('/delete/<int:order_id>')
def delete_order(order_id):
    order = Order.query.get_or_404(order_id)
    db.session.delete(order)
    db.session.commit()
    log_action("Deleted", order.sender)
    return redirect(url_for('index'))

@app.route('/logs')
def view_logs():
    logs = ActionLog.query.order_by(ActionLog.timestamp.desc()).all()
    return render_template('logs.html', logs=logs)

if __name__ == '__main__':
    app.run(debug=True)
