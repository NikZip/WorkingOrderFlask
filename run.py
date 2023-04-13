""" Run this file for running app
Note Set FLASK_APP = run.py, if it's not
"""
from flask.helpers import get_debug_flag
from SiteApp import create_app
from SiteApp.config import ProductionConfig, DevelopmentConfig

CONFIG = DevelopmentConfig if get_debug_flag() else ProductionConfig
# If FLASK_DEBUG set to 0 then prod config else Develop

app = create_app(CONFIG)

if __name__ == '__main__':
    app.run()




