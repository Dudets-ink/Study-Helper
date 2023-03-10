from flask_caching import Cache
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_util_js import FlaskUtilJs

from .utils.config import Config, cache_config


cache = Cache(config=cache_config)
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
flask_ujs = FlaskUtilJs()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    cache.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    login_manager.login_message = 'Please log in'
    
    flask_ujs.init_app(app)
    
    
    from .main_page import main_bp
    app.register_blueprint(main_bp)
    from .user import user_bp
    app.register_blueprint(user_bp)
    
    
    return app
    
    