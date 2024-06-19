
DB_USERNAME = 'farmToMarketDbUser'
DB_PASSWORD = 'pass123'
DB_NAME = 'farmToMarket'


class Config:
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@localhost/{DB_NAME}'
