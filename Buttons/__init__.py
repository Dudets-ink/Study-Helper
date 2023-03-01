from flask_caching import Cache
from flask import Flask

from .config import config, cache_config


cache = Cache(config=cache_config)

def create_app():
    app = Flask(__name__)
    app.config.from_mapping(config)

    cache.init_app(app)
    
    from .main_page import main_bp
    app.register_blueprint(main_bp)
    
    
    return app
    
    