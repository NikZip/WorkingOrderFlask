from flask import Flask
from SiteApp.site.site import site_bp
from SiteApp.config import Config
from .models import db


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    app.register_blueprint(site_bp)
    return app
