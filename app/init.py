from flask import Flask
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
from .models import Base
from config import Config
from .globals import Globals
from .populate_db_script import populate_db


def create_app():
    app = Flask(__name__)
    # setting up configuration of mysql
    app.config.from_object(Config)
    return app


def init_app():
    Globals.app = create_app()

    # setup routes and data-models
    from . import routes, models

    # init DB
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
    Base.metadata.create_all(engine)
    Globals.db = SQLAlchemy(Globals.app)

    # populate DB
    populate_db(Globals.app, Globals.db)
