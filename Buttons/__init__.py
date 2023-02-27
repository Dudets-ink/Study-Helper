def create_app():
    from flask import Flask
    from .config import config
    
    
    app = Flask(__name__)
    
    from .main_page import main_bp
    app.register_blueprint(main_bp)
    app.config.from_mapping(config)
    
    return app