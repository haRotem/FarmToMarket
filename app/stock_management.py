from sqlalchemy.orm import scoped_session, sessionmaker
from .globals import Globals
from .models import Product


class StockManager:
    def __init__(self, farmer_id):
        self.farmer_id = farmer_id
        self.db_session = scoped_session(sessionmaker(bind=Globals.db.engine))

    def add_item(self, item_data):
        new_item = Product(
            name=item_data['name'],
            price=item_data['price'],
            quantity=item_data['quantity'],
            validity=item_data['validity'],
            farmer_id=self.farmer_id
        )
        self.db_session.add(new_item)
        self.db_session.commit()
        return new_item

    def update_item(self, item_id, update_data):
        item = self.db_session.query(Product).filter_by(id=item_id).first()
        if item:
            for key, value in update_data.items():
                setattr(item, key, value)
            self.db_session.commit()
            return item
        return None

    def delete_item(self, item_id):
        item = self.db_session.query(Product).filter_by(id=item_id).first()
        if item:
            self.db_session.delete(item)
            self.db_session.commit()
            return True
        return False

    def list_items(self):
        query = self.db_session.query(Product).filter_by(farmer_id=self.farmer_id)
        return query.all()
