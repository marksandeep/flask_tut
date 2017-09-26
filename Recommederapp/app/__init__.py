from flask import Flask, render_template
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy

from settings import app_config
from .controller import profile 

app = Flask(__name__, template_folder='template')


#db = SQLAlchemy('mysql://root:rootroot@localhost/recommended_shorttv') 

def create_app(config_name=None):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.register_blueprint(profile)
    #app.config.from_object(app_config[config_name])
    app.config.from_object('settings')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    #db.init_app(app)
    
    return app

# @app.route("/")
# def index():
#     return render_template('index.html')






