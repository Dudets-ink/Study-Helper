from flask_caching import Cache
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from .utils.config import config, cache_config


cache = Cache(config=cache_config)
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(config)

    cache.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    
    from .main_page import main_bp
    app.register_blueprint(main_bp)
    
    
    return app
    
    