from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hotel.db'
db = SQLAlchemy(app)

@app.route('/')
def hello_world():
    return ''' 'КОМАНДЫ:
    /shop_list - 
    /trading_list - 
    /product_list'''

    

class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area = db.Column(db.String(25), nullable=False)
    
class Trading(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(20), nullable=False)
    shop = db.Column(db.String(20), nullable=False, unique=True)
    art = db.Column(db.Integer, nullable=False)
    operation = db.Column(db.String(20), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    
    
class Product(db.Model):
    art = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(20), nullable=False)
    name = db.Column(db.String(20), nullable=False)
    unit = db.Column(db.String(20), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    provider = db.Column(db.String(20), nullable=False)
    
@app.route("/shop_list")
def market_list():
    s = []
    for shop in Shop.query.all():
        #print(shop.id, shop.area)
        s.append([shop.id, shop.area])
    return str(s)

@app.route("/trading_list")
def trading_list():
    s = []
    for trading in Trading.query.all():
        #print(trading.id, trading.date, trading.shop, trading.art, trading.operation, trading.quantity, trading.price)
        s.append([trading.id, trading.date, trading.shop, trading.art, trading.operation, trading.quantity, trading.price])
    return str(s)

@app.route("/product_list")
def product_list():
    s = []
    for product in Product.query.all():
        #print(product.art, product.department, product.name, product.unit, product.amount, product.provider)
        s.append([product.art, product.department, product.name, product.unit, product.amount, product.provider])
    return str(s)


if __name__ == '__main__':
    app.run()
    