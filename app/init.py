from flask import Flask
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from .models import Base
from config import Config
from .globals import Globals


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    return app


def init_app():
    Globals.app = create_app()

    # init DB
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
    Base.metadata.create_all(engine)
    Globals.db = SQLAlchemy(Globals.app)

    # set up routes
    from . import routes
