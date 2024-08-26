import datetime
from flask import Flask
from app.forms import ImageDimension
from app.routes import routes
from app.logger import setup_logger

def create_app():
    # init. app
    app = Flask(__name__)
    logger = setup_logger()
    logger.log_text(f"logger setup at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", severity="INFO")
    
    # register blueprints
    app.register_blueprint(routes) 

    return app