from flask import Flask
import os
from flask_migrate import Migrate
from routes import produtos_blueprint
from models import db, init_app, Produtos

app = Flask(__name__)
app.config['SECRET_KEY'] = '5fPxNUWP2Srzded6fayMeA/'
db_path = os.path.join(os.path.dirname(__file__), 'database/product.db')
db_uri = 'sqlite:///{}'.format(db_path)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(produtos_blueprint)
init_app(app)

migrate = Migrate(app, db)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)