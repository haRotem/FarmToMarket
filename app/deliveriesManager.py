from geopy.distance import geodesic
from sqlalchemy.orm import scoped_session, sessionmaker

from .models import Deliveryman, Order, User, Farmer, Product


class DeliveriesManager:
    def __init__(self, db):
        self.db_session = scoped_session(sessionmaker(bind=db.engine))

    def get_address_coordinates(self, address):
        return address.latitude, address.longitude

    def calculate_distance(self, coord1, coord2):
        return geodesic(coord1, coord2).kilometers

    def get_all_orders_in_region(self, region):
        return self.db_session.query(Order).join(User).filter(User.region == region).all()

    def get_orders_ids(self, orders):
        order_ids = []
        for order in orders:
            order_ids.append(order.id)

        return order_ids

    def get_all_order_items(self, orders):
        order_items = []
        for order in orders:
            for item in order.items:
                order_items.append(item)

        return order_items

    def get_all_products_id_in_orders(self, orders):
        products = []
        for order in orders:
            for item in order.items:
                products.append(item.product_id)

        return products

    def get_ordered_farmers(self, farmers, starting_point):
        farmer_distances = []
        for farmer in farmers:
            distance_from_farmer = self.calculate_distance(starting_point, self.get_address_coordinates(farmer.user.address))
            farmer_distance = (farmer, distance_from_farmer)
            farmer_distances.append(farmer_distance)

        farmer_distances.sort(key=lambda x: x[1])

        return farmer_distances

    def get_ordered_customers(self, customers, starting_point):
        customer_distances = []
        for customer in customers:
            distance_from_customer = self.calculate_distance(starting_point, self.get_address_coordinates(customer.user.address))
            customer_distance = (customer, distance_from_customer)
            customer_distances.append(customer_distance)

        customer_distances.sort(key=lambda x: x[1])

        return customer_distances

    def get_delivery_routes(self, request):
        routes = []

        deliveryman_id = request.args.get('deliveryman_id')
        deliveryman = self.db_session.query(Deliveryman).filter_by(id=deliveryman_id).first()

        deliveryman_address = deliveryman.user.address
        region = deliveryman.user.region

        starting_point = self.get_address_coordinates(deliveryman_address)

        # Fetch all orders and order items in the same region
        orders = self.get_all_orders_in_region(region)
        orders_ids = self.get_orders_ids(orders)
        order_items = self.get_all_order_items(orders)

        # Fetch all products in the orders
        products_in_orders = self.get_all_products_id_in_orders(orders)

        # Fetch all unique farmers for the products in the orders
        farmers = self.db_session.query(Farmer).join(Product).filter(Product.id.in_(products_in_orders)).distinct().all()

        # Create a list of (farmer, distance) tuples
        farmer_distances = self.get_ordered_farmers(farmers, starting_point)

        # add pickup routes
        for farmer, distance in farmer_distances:
            farmer_products_to_pickup = {}
            for order_item in order_items:
                if order_item.product.farmer_id == farmer.id:
                    item_amount = farmer_products_to_pickup.get(order_item.product.name)
                    if item_amount:
                        farmer_products_to_pickup[order_item.product.name] = item_amount + order_item.quantity
                    else:
                        farmer_products_to_pickup[order_item.product.name] = order_item.quantity

            routes.append({
                'type': 'pickup',
                'name': farmer.user.username,
                'longitude': farmer.user.address.longitude,
                'latitude': farmer.user.address.latitude,
                'products': farmer_products_to_pickup
            })

        # get last farmer address coordinates
        last_farmer_coordinates = self.get_address_coordinates(farmer_distances[-1][0].user.address)

        customers = self.db_session.query(Order).join(User).filter(Order.id.in_(orders_ids))
        customer_distances = self.get_ordered_customers(customers, last_farmer_coordinates)

        for customer, customer_distance in customer_distances:
            customer_products_to_deliver = {}
            for order_item in order_items:
                if order_item.order.user_id == customer.user.id:
                    item_amount = customer_products_to_deliver.get(order_item.product.name)
                    if item_amount:
                        customer_products_to_deliver[order_item.product.name] += item_amount + order_item.quantity
                    else:
                        customer_products_to_deliver[order_item.product.name] = order_item.quantity
            routes.append({
                'type': 'delivery',
                'name': customer.user.username,
                'longitude': customer.user.address.longitude,
                'latitude': customer.user.address.latitude,
                'products': customer_products_to_deliver
            })

        return routes
