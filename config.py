
DB_USERNAME = 'technicalUser'
DB_PASSWORD = 'pass'
DB_NAME = 'v1'


class Config:
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@localhost/{DB_NAME}'
