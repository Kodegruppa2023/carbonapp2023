from flask import Flask

application = Flask(__name__)

application.config['SECRET_KEY'] = 'adddd7987d5400199c650f5de1393135908d2605a8b67824'

from capp.home.routes import home
from capp.methodology.routes import methodology
from capp.carbon_app.routes import carbon_app 

application.register_blueprint(home)
application.register_blueprint(methodology)
application.register_blueprint(carbon_app)
