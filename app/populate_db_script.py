from .models import ProductDetail, User, Address, Farmer, Deliveryman, Product

productDetails = {
    'v1': {'name': 'Asparagos', 'image': 'asparagos.jpg', 'price': 34.9, 'category': 'vegetable'},
    'v2': {'name': 'Bean', 'image': 'bean.jpg', 'price': 88.3, 'category': 'vegetable'},
    'v3': {'name': 'Artichoke', 'image': 'artichoke.jpg', 'price': 9.4, 'category': 'vegetable'},
    'v4': {'name': 'Sweet Potato', 'image': 'sweet_potato.jpg', 'price': 10.2, 'category': 'vegetable'},
    'v5': {'name': 'Onion', 'image': 'onion.jpg', 'price': 5.1, 'category': 'vegetable'},
    'v6': {'name': 'Red Onion', 'image': 'red_onion.jpg', 'price': 8.6, 'category': 'vegetable'},
    'v7': {'name': 'Broccoli', 'image': 'broccoli.jpg', 'price': 21, 'category': 'vegetable'},
    'v8': {'name': 'Carrot', 'image': 'carrot.jpg', 'price': 5.2, 'category': 'vegetable'},
    'v9': {'name': 'Pumpkin', 'image': 'pumpkin.jpg', 'price': 11.7, 'category': 'vegetable'},
    'v10': {'name': 'Zucchini', 'image': 'zucchini.jpg', 'price': 6.2, 'category': 'vegetable'},
    'v11': {'name': 'Eggplant', 'image': 'eggplant.jpg', 'price': 7, 'category': 'vegetable'},
    'v12': {'name': 'Red Cabbage', 'image': 'red_cabbage.jpg', 'price': 4.5, 'category': 'vegetable'},
    'v13': {'name': 'White Cabbage', 'image': 'white_cabbage.jpg', 'price': 3.5, 'category': 'vegetable'},
    'v14': {'name': 'Cauliflower', 'image': 'cauliflower.jpg', 'price': 9, 'category': 'vegetable'},
    'v15': {'name': 'Cucumber', 'image': 'cucumber.jpg', 'price': 4.9, 'category': 'vegetable'},
    'v16': {'name': 'Beet', 'image': 'beet.jpg', 'price': 6, 'category': 'vegetable'},
    'v17': {'name': 'Tomato', 'image': 'tomato.jpg', 'price': 7.7, 'category': 'vegetable'},
    'v18': {'name': 'Cherry Tomato', 'image': 'cherry_tomato.jpg', 'price': 16.5, 'category': 'vegetable'},
    'v19': {'name': 'Red Pepper', 'image': 'red_pepper.jpg', 'price': 9.5, 'category': 'vegetable'},
    'v20': {'name': 'Hot Pepper', 'image': 'hot_pepper.jpg', 'price': 7.5, 'category': 'vegetable'},
    'v22': {'name': 'Orange Pepper', 'image': 'orange_pepper.jpg', 'price': 10.5, 'category': 'vegetable'},
    'v23': {'name': 'Yellow Pepper', 'image': 'yellow_pepper.jpg', 'price': 10.5, 'category': 'vegetable'},
    'v24': {'name': 'Kolorabi', 'image': 'kolorabi.jpg', 'price': 6, 'category': 'vegetable'},
    'v25': {'name': 'Squash', 'image': 'squash.jpg', 'price': 5.3, 'category': 'vegetable'},
    'v26': {'name': 'Garlic', 'image': 'garlic.jpg', 'price': 9.9, 'category': 'vegetable'},
    'v27': {'name': 'Corn', 'image': 'corn.jpg', 'price': 7, 'category': 'vegetable'},
    'v28': {'name': 'Potato', 'image': 'potato.jpg', 'price': 5.1, 'category': 'vegetable'},
    'f1': {'name': 'Watermelon', 'image': 'watermelon.jpg', 'price': 6.4, 'category': 'fruit'},
    'f2': {'name': 'Pear', 'image': 'pear.jpg', 'price': 9.1, 'category': 'fruit'},
    'f3': {'name': 'Blueberries', 'image': 'blueberries.jpg', 'price': 40.2, 'category': 'fruit'},
    'f4': {'name': 'Pineapple', 'image': 'pineapple.jpg', 'price': 21.8, 'category': 'fruit'},
    'f5': {'name': 'Peach', 'image': 'peach.jpg', 'price': 18.9, 'category': 'fruit'},
    'f6': {'name': 'Grapefruit', 'image': 'grapefruit.jpg', 'price': 6.1, 'category': 'fruit'},
    'f7': {'name': 'Banana', 'image': 'banana.jpg', 'price': 5, 'category': 'fruit'},
    'f8': {'name': 'Melon', 'image': 'melon.jpg', 'price': 6.7, 'category': 'fruit'},
    'f9': {'name': 'Sabres', 'image': 'sabres.jpg', 'price': 27.6, 'category': 'fruit'},
    'f10': {'name': 'Pomelo', 'image': 'pomelo.jpg', 'price': 6.9, 'category': 'fruit'},
    'f11': {'name': 'Kiwi', 'image': 'kiwi.jpg', 'price': 13.2, 'category': 'fruit'},
    'f12': {'name': 'Clementine', 'image': 'clementine.jpg', 'price': 6.5, 'category': 'fruit'},
    'f13': {'name': 'Loquat', 'image': 'loquat.jpg', 'price': 28.4, 'category': 'fruit'},
    'f14': {'name': 'Strawberry', 'image': 'strawberry.jpg', 'price': 30, 'category': 'fruit'},
    'f15': {'name': 'Orange', 'image': 'orange.jpg', 'price': 5.7, 'category': 'fruit'},
    'f16': {'name': 'Grand Smith Apple', 'image': 'apple_grand_smith.jpg', 'price': 10.2, 'category': 'fruit'},
    'f17': {'name': 'Hermon Apple', 'image': 'apple_hermon.jpg', 'price': 9.9, 'category': 'fruit'},
    'f18': {'name': 'Jonatan Apple', 'image': 'apple_jonatan.jpg', 'price': 9.8, 'category': 'fruit'},
    'f19': {'name': 'Pink Lady Apple', 'image': 'apple_pink_lady.jpg', 'price': 9.6, 'category': 'fruit'},
    'f20': {'name': 'Lemon', 'image': 'lemon.jpg', 'price': 5.4, 'category': 'fruit'},
    'l1': {'name': 'Arugula', 'image': 'arugula.jpg', 'price': 5, 'category': 'leafs_and_mushrooms'},
    'l2': {'name': 'Bok Choi', 'image': 'bok_choi.jpg', 'price': 12.6, 'category': 'leafs_and_mushrooms'},
    'l3': {'name': 'Caesars Hearts', 'image': 'caesars_hearts.jpg', 'price': 7, 'category': 'leafs_and_mushrooms'},
    'l4': {'name': 'Champanion Mushroom', 'image': 'champanion_mushrooms.jpg', 'price': 10.3,
           'category': 'leafs_and_mushrooms'},
    'l5': {'name': 'Coriander', 'image': 'coriander.jpg', 'price': 2.7, 'category': 'leafs_and_mushrooms'},
    'l6': {'name': 'Curled Lettuce', 'image': 'curled_lettuce.jpg', 'price': 4.9, 'category': 'leafs_and_mushrooms'},
    'l7': {'name': 'Mint', 'image': 'mint.jpg', 'price': 3.8, 'category': 'leafs_and_mushrooms'},
    'l8': {'name': 'King Forest Mushroom', 'image': 'king_forest_mushrooms.jpg', 'price': 14.7,
           'category': 'leafs_and_mushrooms'},
    'l9': {'name': 'Portobello Mushroom', 'image': 'mushroom_portobello.jpg', 'price': 8.2,
           'category': 'leafs_and_mushrooms'},
    'l10': {'name': 'Rocket', 'image': 'rocket.jpg', 'price': 4.1, 'category': 'leafs_and_mushrooms'},
    'l11': {'name': 'Romaine Lettuce', 'image': 'romaine_lettuce.jpg', 'price': 8.8, 'category': 'leafs_and_mushrooms'},
    'l12': {'name': 'Rosemary', 'image': 'rosemary.jpg', 'price': 5.9, 'category': 'leafs_and_mushrooms'},
    'l13': {'name': 'Round Iceberg Lettuce', 'image': 'round_iceberg_lettuce.jpg', 'price': 8.5,
            'category': 'leafs_and_mushrooms'},
    'l14': {'name': 'Spinach', 'image': 'spinach.jpg', 'price': 11, 'category': 'leafs_and_mushrooms'},
    'l15': {'name': 'Thyme', 'image': 'thyme.jpg', 'price': 3.9, 'category': 'leafs_and_mushrooms'}
}


def populate_product_details(app, db):
    with app.app_context():
        for sku, productDetail in productDetails.items():
            existing_prod_detail = db.session.query(ProductDetail).filter_by(sku=sku).first()
            if not existing_prod_detail:
                product_detail = ProductDetail(sku=sku, name=productDetail['name'], imageName=productDetail['image'],
                                               price=productDetail['price'], category=productDetail['category'])
                db.session.add(product_detail)
        db.session.commit()


addresses = {
    'address1': {'postalCode': 5252102, 'city': 'Ramat Gan', 'street': 'Bialik', 'houseNumber': '10',
                 'latitude': 32.0851, 'longitude': 34.8153},
    'address2': {'postalCode': 7102001, 'city': 'Rishon LeZion', 'street': 'HaRav Herzog', 'houseNumber': '17',
                 'latitude': 31.9679, 'longitude': 34.7986},
    'address3': {'postalCode': 6814808, 'city': 'Tel Aviv', 'street': 'King George', 'houseNumber': '22',
                 'latitude': 32.0737, 'longitude': 34.7756},
    'address4': {'postalCode': 6814809, 'city': 'Tel Aviv', 'street': 'Ibn Gabirol', 'houseNumber': '88',
                 'latitude': 32.0809, 'longitude': 34.7811},
    'address5': {'postalCode': 3466215, 'city': 'Holon', 'street': 'HaRav Kook', 'houseNumber': '30',
                 'latitude': 32.0117, 'longitude': 34.7761},
    'address6': {'postalCode': 6814807, 'city': 'Tel Aviv', 'street': 'Herzl', 'houseNumber': '11', 'latitude': 32.0679,
                 'longitude': 34.7768},
    'address7': {'postalCode': 4217603, 'city': 'Herzliya', 'street': 'HaSharon', 'houseNumber': '5',
                 'latitude': 32.1665, 'longitude': 34.8284},
    'address8': {'postalCode': 4810046, 'city': 'Bnei Brak', 'street': 'Rabbi Akiva', 'houseNumber': '14',
                 'latitude': 32.0857, 'longitude': 34.8368},
    'address9': {'postalCode': 6814801, 'city': 'Tel Aviv', 'street': 'Rothschild', 'houseNumber': '1',
                 'latitude': 32.0666, 'longitude': 34.7734},
    'address10': {'postalCode': 6814804, 'city': 'Tel Aviv', 'street': 'Nahalat Binyamin', 'houseNumber': '2',
                  'latitude': 32.0674, 'longitude': 34.7722},
    'address11': {'postalCode': 6814802, 'city': 'Tel Aviv', 'street': 'Ben Yehuda', 'houseNumber': '15',
                  'latitude': 32.0751, 'longitude': 34.7697},
    'address12': {'postalCode': 6814803, 'city': 'Tel Aviv', 'street': 'Allenby', 'houseNumber': '12',
                  'latitude': 32.0713, 'longitude': 34.7750},
    'address13': {'postalCode': 6814805, 'city': 'Tel Aviv', 'street': 'Dizengoff', 'houseNumber': '50',
                  'latitude': 32.0767, 'longitude': 34.7742},
    'address14': {'postalCode': 4951204, 'city': 'Petah Tikva', 'street': 'HaBarzel', 'houseNumber': '6',
                  'latitude': 32.0925, 'longitude': 34.8880},
    'address15': {'postalCode': 6814806, 'city': 'Tel Aviv', 'street': 'Frishman', 'houseNumber': '18',
                  'latitude': 32.0801, 'longitude': 34.7716},
    'address16': {'postalCode': 6814810, 'city': 'Tel Aviv', 'street': 'Allenby', 'houseNumber': '34',
                  'latitude': 32.0719, 'longitude': 34.7765},

    'address17': {'postalCode': 2222201, 'city': 'Metula', 'street': 'HaPalmach', 'houseNumber': '3',
                  'latitude': 33.2827, 'longitude': 35.5685},
    'address18': {'postalCode': 2282302, 'city': 'Kiryat Shmona', 'street': 'HaGefen', 'houseNumber': '10',
                  'latitude': 33.2076, 'longitude': 35.5714},
    'address19': {'postalCode': 2243403, 'city': 'Maalot-Tarshiha', 'street': 'HaMaccabi', 'houseNumber': '6',
                  'latitude': 33.0061, 'longitude': 35.2803},
    'address20': {'postalCode': 2245604, 'city': 'Safed', 'street': 'HaAri', 'houseNumber': '17', 'latitude': 32.9684,
                  'longitude': 35.4952},
    'address21': {'postalCode': 2244405, 'city': 'Karmiel', 'street': 'HaGefen', 'houseNumber': '30',
                  'latitude': 32.9192, 'longitude': 35.3081},
    'address22': {'postalCode': 2280306, 'city': 'Katzrin', 'street': 'HaYovel', 'houseNumber': '5',
                  'latitude': 32.9867, 'longitude': 35.6989},
    'address23': {'postalCode': 2285207, 'city': 'Metula', 'street': 'HaAlonim', 'houseNumber': '12',
                  'latitude': 33.2679, 'longitude': 35.5774},
    'address24': {'postalCode': 2290308, 'city': 'Kiryat Shmona', 'street': 'HaTavor', 'houseNumber': '21',
                  'latitude': 33.2098, 'longitude': 35.5680},
    'address25': {'postalCode': 2291509, 'city': 'Rosh Pina', 'street': 'HaEmek', 'houseNumber': '7',
                  'latitude': 32.9673, 'longitude': 35.5332},
    'address26': {'postalCode': 2222210, 'city': 'Metula', 'street': 'HaShayish', 'houseNumber': '14',
                  'latitude': 33.2785, 'longitude': 35.5727},
    'address27': {'postalCode': 2282301, 'city': 'Kiryat Shmona', 'street': 'HaRishonim', 'houseNumber': '2',
                  'latitude': 33.2134, 'longitude': 35.5651},
    'address28': {'postalCode': 2243402, 'city': 'Maalot-Tarshiha', 'street': 'HaHaroshet', 'houseNumber': '9',
                  'latitude': 33.0138, 'longitude': 35.2718},
    'address29': {'postalCode': 2245603, 'city': 'Safed', 'street': 'HaAri', 'houseNumber': '25', 'latitude': 32.9707,
                  'longitude': 35.4971},
    'address30': {'postalCode': 2244404, 'city': 'Karmiel', 'street': 'HaCarmel', 'houseNumber': '40',
                  'latitude': 32.9234, 'longitude': 35.2994},
    'address31': {'postalCode': 2280305, 'city': 'Katzrin', 'street': 'HaMaayan', 'houseNumber': '13',
                  'latitude': 32.9821, 'longitude': 35.6887},
    'address32': {'postalCode': 2285206, 'city': 'Metula', 'street': 'HaErez', 'houseNumber': '18', 'latitude': 33.2696,
                  'longitude': 35.5701},

    'address33': {'postalCode': 7790411, 'city': 'Beer Sheva', 'street': 'HaRav Hacohen', 'houseNumber': '3',
                  'latitude': 31.2537, 'longitude': 34.7910},
    'address34': {'postalCode': 7926432, 'city': 'Netivot', 'street': 'HaTamar', 'houseNumber': '10',
                  'latitude': 31.4202, 'longitude': 34.5959},
    'address35': {'postalCode': 7913603, 'city': 'Sderot', 'street': 'HaShita', 'houseNumber': '6', 'latitude': 31.5198,
                  'longitude': 34.5917},
    'address36': {'postalCode': 7911014, 'city': 'Ashkelon', 'street': 'HaGefen', 'houseNumber': '17',
                  'latitude': 31.6656, 'longitude': 34.5702},
    'address37': {'postalCode': 7943605, 'city': 'Ofakim', 'street': 'HaAyalon', 'houseNumber': '30',
                  'latitude': 31.3114, 'longitude': 34.6171},
    'address38': {'postalCode': 7917606, 'city': 'Kiryat Gat', 'street': 'HaYarden', 'houseNumber': '5',
                  'latitude': 31.6087, 'longitude': 34.7659},
    'address39': {'postalCode': 7990407, 'city': 'Nirim', 'street': 'HaGefen', 'houseNumber': '12', 'latitude': 31.3429,
                  'longitude': 34.4726},
    'address40': {'postalCode': 7920308, 'city': 'Netiv HaAsara', 'street': 'HaMaayan', 'houseNumber': '21',
                  'latitude': 31.5336, 'longitude': 34.5071},
    'address41': {'postalCode': 7913009, 'city': 'Kibbutz Kfar Aza', 'street': 'HaErez', 'houseNumber': '7',
                  'latitude': 31.4694, 'longitude': 34.5818},
    'address42': {'postalCode': 7942603, 'city': 'Eshkolot', 'street': 'HaCarmel', 'houseNumber': '14',
                  'latitude': 31.3947, 'longitude': 34.5902},
    'address43': {'postalCode': 7926331, 'city': 'Nevatim', 'street': 'HaDekel', 'houseNumber': '2',
                  'latitude': 31.1832, 'longitude': 34.7057},
    'address44': {'postalCode': 7911012, 'city': 'Ashdod', 'street': 'HaTavor', 'houseNumber': '9', 'latitude': 31.7874,
                  'longitude': 34.6497},
    'address45': {'postalCode': 7913601, 'city': 'Sderot', 'street': 'HaArazim', 'houseNumber': '25',
                  'latitude': 31.5176, 'longitude': 34.5901},
    'address46': {'postalCode': 7914004, 'city': 'Beit HaGadi', 'street': 'HaTzav', 'houseNumber': '40',
                  'latitude': 31.5394, 'longitude': 34.6051},
    'address47': {'postalCode': 7992405, 'city': 'Alumim', 'street': 'HaDekel', 'houseNumber': '13',
                  'latitude': 31.3308, 'longitude': 34.4913},
    'address48': {'postalCode': 7924406, 'city': 'Nirim', 'street': 'HaRishonim', 'houseNumber': '18',
                  'latitude': 31.3121, 'longitude': 34.4690}
}


def populate_addresses(app, db):
    with app.app_context():
        for _, address in addresses.items():
            existing_address = db.session.query(Address).filter_by(postalCode=address['postalCode']).first()
            if not existing_address:
                address_to_create = Address(postalCode=address['postalCode'], city=address['city'],
                                            street=address['street'],
                                            houseNumber=address['houseNumber'], latitude=address['latitude'],
                                            longitude=address['longitude'])
                db.session.add(address_to_create)
        db.session.commit()


users = {
    'john_North_Deliveryman': {'username': 'john', 'email': 'john@doe.com', 'phoneNumber': '0541234567',
                               'region': 'North', 'postalCode': 2222201},
    'Liam_South_Deliveryman': {'username': 'liam', 'email': 'liam@gmail.com', 'phoneNumber': '0541237890',
                               'region': 'South', 'postalCode': 7790411},
    'Noah_Center_Deliveryman': {'username': 'noah', 'email': 'noah@gmail.com', 'phoneNumber': '0541235678',
                                'region': 'Center', 'postalCode': 5252102},

    'Oliver_North_Farmer': {'username': 'oliver', 'email': 'oliver@gmail.com', 'phoneNumber': '0541232345',
                            'region': 'North', 'postalCode': 2282302},
    'James_North_Farmer': {'username': 'james', 'email': 'james@gmail.com', 'phoneNumber': '0541236789',
                           'region': 'North', 'postalCode': 2243403},
    'Elijah_North_Farmer': {'username': 'elijah', 'email': 'elijah@gmail.com', 'phoneNumber': '0541233456',
                            'region': 'North', 'postalCode': 2245604},
    'Emma_North_Farmer': {'username': 'emma', 'email': 'emma@gmail.com', 'phoneNumber': '0541233456', 'region': 'North',
                          'postalCode': 2244405},
    'Evelyn_North_Farmer': {'username': 'evelyn', 'email': 'evelyn@gmail.com', 'phoneNumber': '0541238901',
                            'region': 'North', 'postalCode': 2280306},

    'Amelia_South_Farmer': {'username': 'amelia', 'email': 'amelia@gmail.com', 'phoneNumber': '0541234567',
                            'region': 'South', 'postalCode': 7926432},
    'Mateo_South_Farmer': {'username': 'mateo', 'email': 'mateo@gmail.com', 'phoneNumber': '0541238901',
                           'region': 'South', 'postalCode': 7913603},
    'Benjamin_South_Farmer': {'username': 'benjamin', 'email': 'benjamin@gmail.com', 'phoneNumber': '0541234567',
                              'region': 'South', 'postalCode': 7911014},
    'Levi_South_Farmer': {'username': 'levi', 'email': 'levi@gmail.com', 'phoneNumber': '0541232345', 'region': 'South',
                          'postalCode': 7943605},

    'Jack_South_Farmer': {'username': 'jack', 'email': 'jack@gmail.com', 'phoneNumber': '0541236789', 'region': 'South',
                          'postalCode': 7917606},

    'Ezra_Center_Farmer': {'username': 'ezra', 'email': 'ezra@gmail.com', 'phoneNumber': '0541233456',
                           'region': 'Center', 'postalCode': 7102001},
    'Michael_Center_Farmer': {'username': 'michael', 'email': 'michael@gmail.com', 'phoneNumber': '0541238901',
                              'region': 'Center', 'postalCode': 6814808},
    'Daniel_Center_Farmer': {'username': 'daniel', 'email': 'daniel@gmail.com', 'phoneNumber': '0541234567',
                             'region': 'Center', 'postalCode': 6814809},
    'Samuel_Center_Farmer': {'username': 'samuel', 'email': 'samuel@gmail.com', 'phoneNumber': '0541232345',
                             'region': 'Center', 'postalCode': 3466215},
    'Alexander_Center_Farmer': {'username': 'alexander', 'email': 'alexander@gmail.com', 'phoneNumber': '0541236789',
                                'region': 'Center', 'postalCode': 6814807},

    'Liam': {'username': 'liam', 'email': 'liam@gmail.com', 'phoneNumber': '0541237899', 'region': 'North',
             'postalCode': 2285207},
    'Noah': {'username': 'noah', 'email': 'noah@gmail.com', 'phoneNumber': '0541235670', 'region': 'North',
             'postalCode': 2290308},
    'Oliver': {'username': 'oliver', 'email': 'oliver@gmail.com', 'phoneNumber': '0541232346', 'region': 'North',
               'postalCode': 2291509},
    'Naomi': {'username': 'naomi', 'email': 'naomi@gmail.com', 'phoneNumber': '0541237890', 'region': 'North',
              'postalCode': 2222210},
    'Victoria': {'username': 'victoria', 'email': 'victoria@gmail.com', 'phoneNumber': '0541235678', 'region': 'North',
                 'postalCode': 2282301},
    'Stella': {'username': 'stella', 'email': 'stella@gmail.com', 'phoneNumber': '0541233456', 'region': 'North',
               'postalCode': 2243402},
    'Elena': {'username': 'elena', 'email': 'elena@gmail.com', 'phoneNumber': '0541232345', 'region': 'North',
              'postalCode': 2245603},
    'Hannah': {'username': 'hannah', 'email': 'hannah@gmail.com', 'phoneNumber': '0541231234', 'region': 'North',
               'postalCode': 2244404},
    'Valentina': {'username': 'valentina', 'email': 'valentina@gmail.com', 'phoneNumber': '0541238765',
                  'region': 'North', 'postalCode': 2280305},
    'Maya': {'username': 'maya', 'email': 'maya@gmail.com', 'phoneNumber': '0541239876', 'region': 'North',
             'postalCode': 2285206},

    'Asher': {'username': 'asher', 'email': 'asher@gmail.com', 'phoneNumber': '0541233456', 'region': 'Center',
              'postalCode': 4217603},
    'Ethan': {'username': 'ethan', 'email': 'ethan@gmail.com', 'phoneNumber': '0541238901', 'region': 'Center',
              'postalCode': 4810046},
    'John': {'username': 'john', 'email': 'john@gmail.com', 'phoneNumber': '0541234567', 'region': 'Center',
             'postalCode': 6814801},
    'David': {'username': 'david', 'email': 'david@gmail.com', 'phoneNumber': '0541232345', 'region': 'Center',
              'postalCode': 6814804},
    'Jackson': {'username': 'jackson', 'email': 'jackson@gmail.com', 'phoneNumber': '0541236789', 'region': 'Center',
                'postalCode': 6814802},
    'Zoey': {'username': 'zoey', 'email': 'zoey@gmail.com', 'phoneNumber': '0541234567', 'region': 'Center',
             'postalCode': 6814803},
    'Delilah': {'username': 'delilah', 'email': 'delilah@gmail.com', 'phoneNumber': '0541236789', 'region': 'Center',
                'postalCode': 6814805},
    'Leah': {'username': 'leah', 'email': 'leah@gmail.com', 'phoneNumber': '0541237891', 'region': 'Center',
             'postalCode': 4951204},
    'Madeline': {'username': 'madeline', 'email': 'madeline@gmail.com', 'phoneNumber': '0541234321', 'region': 'Center',
                 'postalCode': 6814806},
    'Natalia': {'username': 'natalia', 'email': 'natalia@gmail.com', 'phoneNumber': '0541235432', 'region': 'Center',
                'postalCode': 6814810},

    'Luna': {'username': 'luna', 'email': 'luna@gmail.com', 'phoneNumber': '0541232345', 'region': 'South',
             'postalCode': 7990407},
    'Sofia': {'username': 'sofia', 'email': 'sofia@gmail.com', 'phoneNumber': '0541236789', 'region': 'South',
              'postalCode': 7920308},
    'Camila': {'username': 'camila', 'email': 'camila@gmail.com', 'phoneNumber': '0541233456', 'region': 'South',
               'postalCode': 7913009},
    'Eleanor': {'username': 'eleanor', 'email': 'eleanor@gmail.com', 'phoneNumber': '0541238901', 'region': 'South',
                'postalCode': 7942603},
    'Mia': {'username': 'mia', 'email': 'mia@gmail.com', 'phoneNumber': '0541234567', 'region': 'South',
            'postalCode': 7926331},
    'Lily': {'username': 'lily', 'email': 'lily@gmail.com', 'phoneNumber': '0541232345', 'region': 'South',
             'postalCode': 7911012},
    'Aria': {'username': 'aria', 'email': 'aria@gmail.com', 'phoneNumber': '0541236789', 'region': 'South',
             'postalCode': 7913601},
    'Scarlett': {'username': 'scarlett', 'email': 'scarlett@gmail.com', 'phoneNumber': '0541233456', 'region': 'South',
                 'postalCode': 7914004},
    'Ariana': {'username': 'ariana', 'email': 'ariana@gmail.com', 'phoneNumber': '0541236543', 'region': 'South',
               'postalCode': 7992405},
    'Lydia': {'username': 'lydia', 'email': 'lydia@gmail.com', 'phoneNumber': '0541237654', 'region': 'South',
              'postalCode': 7924406},
}
usersId = {}


def populate_users(app, db):
    with app.app_context():
        for name, user in users.items():
            user_record = db.session.query(User).filter_by(username=user['username']).first()
            if not user_record:
                user_record = User(username=user['username'], email=user['email'], phoneNumber=user['phoneNumber'],
                                   region=user['region'], postalCode=user['postalCode'])
                db.session.add(user_record)
                db.session.commit()

            usersId[name] = user_record.id


farmers = [
    'Oliver_North_Farmer',
    'James_North_Farmer',
    'Elijah_North_Farmer',
    'Emma_North_Farmer',
    'Evelyn_North_Farmer',
    'Amelia_South_Farmer',
    'Mateo_South_Farmer',
    'Benjamin_South_Farmer',
    'Levi_South_Farmer',
    'Jack_South_Farmer',
    'Ezra_Center_Farmer',
    'Michael_Center_Farmer',
    'Daniel_Center_Farmer',
    'Samuel_Center_Farmer',
    'Alexander_Center_Farmer'
]
farmersId = {}


def populate_farmers(app, db):
    with app.app_context():
        for farmer in farmers:
            farmer_record = db.session.query(Farmer).filter_by(user_id=usersId[farmer]).first()
            if not farmer_record:
                farmer_record = Farmer(user_id=usersId[farmer])
                db.session.add(farmer_record)
                db.session.commit()

            farmersId[farmer] = farmer_record.id


deliverymen = ['john_North_Deliveryman', 'Liam_South_Deliveryman', 'Noah_Center_Deliveryman']


def populate_deliverymen(app, db):
    with app.app_context():
        for deliveryman in deliverymen:
            deliveryman_record = db.session.query(Deliveryman).filter_by(user_id=usersId[deliveryman]).first()
            if not deliveryman_record:
                deliveryman_record = Deliveryman(user_id=usersId[deliveryman])
                db.session.add(deliveryman_record)
        db.session.commit()

products = [
    {'SKU': 'l2', 'name': 'Bok choi', 'quantity': 100, 'validity': '24-08-30', 'farmer': 'Oliver_North_Farmer'},
    {'SKU': 'l7', 'name': 'Mint', 'quantity': 112, 'validity': '24-09-16', 'farmer': 'Oliver_North_Farmer'},
    {'SKU': 'l6', 'name': 'Curled Lettuce', 'quantity': 90, 'validity': '24-09-12', 'farmer': 'Oliver_North_Farmer'},
    {'SKU': 'f6', 'name': 'Grapefruit', 'quantity': 108, 'validity': '24-08-20', 'farmer': 'Oliver_North_Farmer'},
    {'SKU': 'l8', 'name': 'Mushroom King of The Forest', 'quantity': 115, 'validity': '24-09-25',
     'farmer': 'Oliver_North_Farmer'},
    {'SKU': 'l9', 'name': 'Portobello Mushroom', 'quantity': 190, 'validity': '24-09-15',
     'farmer': 'Oliver_North_Farmer'},
    {'SKU': 'f8', 'name': 'Melon', 'quantity': 200, 'validity': '24-08-30', 'farmer': 'Oliver_North_Farmer'},
    {'SKU': 'f9', 'name': 'Sabers', 'quantity': 110, 'validity': '24-09-16', 'farmer': 'Oliver_North_Farmer'},
    {'SKU': 'v28', 'name': 'Potato', 'quantity': 239, 'validity': '24-08-19', 'farmer': 'Oliver_North_Farmer'},
    {'SKU': 'f7', 'name': 'Banana', 'quantity': 188, 'validity': '24-09-25', 'farmer': 'Oliver_North_Farmer'},
    {'SKU': 'f12', 'name': 'clementine', 'quantity': 238, 'validity': '24-08-19', 'farmer': 'Oliver_North_Farmer'},
    {'SKU': 'f1', 'name': 'watermelon', 'quantity': 239, 'validity': '24-10-01', 'farmer': 'Oliver_North_Farmer'},
    {'SKU': 'f3', 'name': 'Blueberries', 'quantity': 113, 'validity': '24-09-13', 'farmer': 'Oliver_North_Farmer'},
    {'SKU': 'f4', 'name': 'pineapple', 'quantity': 128, 'validity': '24-09-03', 'farmer': 'Oliver_North_Farmer'},


    {'SKU': 'f18', 'name': 'Jonathan Apple', 'quantity': 646, 'validity': '24-08-22', 'farmer': 'James_North_Farmer'},
    {'SKU': 'f19', 'name': 'Pink Lady Apple', 'quantity': 736, 'validity': '24-09-30', 'farmer': 'James_North_Farmer'},
    {'SKU': 'l10', 'name': 'Rocket', 'quantity': 279, 'validity': '24-10-03', 'farmer': 'James_North_Farmer'},
    {'SKU': 'v12', 'name': 'Red Cabbage', 'quantity': 325, 'validity': '24-08-06', 'farmer': 'James_North_Farmer'},
    {'SKU': 'v15', 'name': 'Cucumber', 'quantity': 460, 'validity': '24-08-01', 'farmer': 'James_North_Farmer'},
    {'SKU': 'v3', 'name': 'Artichoke', 'quantity': 543, 'validity': '24-10-27', 'farmer': 'James_North_Farmer'},
    {'SKU': 'v14', 'name': 'cauliflower', 'quantity': 207, 'validity': '24-09-18', 'farmer': 'James_North_Farmer'},
    {'SKU': 'v22', 'name': 'Orange pepper', 'quantity': 124, 'validity': '24-09-23', 'farmer': 'James_North_Farmer'},
    {'SKU': 'v23', 'name': 'Yellow pepper', 'quantity': 148, 'validity': '24-10-25', 'farmer': 'James_North_Farmer'},
    {'SKU': 'v24', 'name': 'Kolorbi', 'quantity': 240, 'validity': '24-09-08', 'farmer': 'James_North_Farmer'},
    {'SKU': 'f16', 'name': 'Grand Smith apple', 'quantity': 207, 'validity': '24-08-23', 'farmer': 'James_North_Farmer'},
    {'SKU': 'v4', 'name': 'sweet potato', 'quantity': 179, 'validity': '24-08-27', 'farmer': 'James_North_Farmer'},

    {'SKU': 'v2', 'name': 'Bean', 'quantity': 282, 'validity': '24-10-15', 'farmer': 'Elijah_North_Farmer'},
    {'SKU': 'v26', 'name': 'Garlic', 'quantity': 653, 'validity': '24-09-28', 'farmer': 'Elijah_North_Farmer'},
    {'SKU': 'l15', 'name': 'Thyme', 'quantity': 300, 'validity': '24-10-02', 'farmer': 'Elijah_North_Farmer'},
    {'SKU': 'f10', 'name': 'Pomelo', 'quantity': 239, 'validity': '24-09-18', 'farmer': 'Elijah_North_Farmer'},
    {'SKU': 'v9', 'name': 'pumpkin', 'quantity': 809, 'validity': '24-10-23', 'farmer': 'Elijah_North_Farmer'},
    {'SKU': 'v17', 'name': 'Tomato', 'quantity': 536, 'validity': '24-08-28', 'farmer': 'Elijah_North_Farmer'},
    {'SKU': 'v27', 'name': 'Corn', 'quantity': 634, 'validity': '24-09-19', 'farmer': 'Elijah_North_Farmer'},
    {'SKU': 'v8', 'name': 'carrot', 'quantity': 238, 'validity': '24-09-30', 'farmer': 'Elijah_North_Farmer'},
    {'SKU': 'f13', 'name': 'loquat', 'quantity': 284, 'validity': '24-09-11', 'farmer': 'Elijah_North_Farmer'},
    {'SKU': 'l3', 'name': "Caesar's hearts", 'quantity': 382, 'validity': '24-09-22', 'farmer': 'Elijah_North_Farmer'},
    {'SKU': 'f15', 'name': 'orange', 'quantity': 587, 'validity': '24-08-07', 'farmer': 'Elijah_North_Farmer'},
    {'SKU': 'f20', 'name': 'lemon', 'quantity': 554, 'validity': '24-08-01', 'farmer': 'Elijah_North_Farmer'},
    {'SKU': 'l12', 'name': 'Rosemary', 'quantity': 589, 'validity': '24-09-12', 'farmer': 'Elijah_North_Farmer'},
    {'SKU': 'f5', 'name': 'peach', 'quantity': 189, 'validity': '24-10-30', 'farmer': 'Elijah_North_Farmer'},


    {'SKU': 'v19', 'name': 'Red pepper', 'quantity': 316, 'validity': '24-10-19', 'farmer': 'Emma_North_Farmer'},
    {'SKU': 'v20', 'name': 'Hot Pepper', 'quantity': 384, 'validity': '24-09-26', 'farmer': 'Emma_North_Farmer'},
    {'SKU': 'l13', 'name': 'Round iceberg lettuce', 'quantity': 833, 'validity': '24-10-19',
     'farmer': 'Emma_North_Farmer'},
    {'SKU': 'l14', 'name': 'Spinach', 'quantity': 639, 'validity': '24-08-27', 'farmer': 'Emma_North_Farmer'},
    {'SKU': 'l11', 'name': 'Romaine lettuce', 'quantity': 682, 'validity': '24-08-09', 'farmer': 'Emma_North_Farmer'},
    {'SKU': 'v18', 'name': 'Cherry tomato', 'quantity': 214, 'validity': '24-10-13', 'farmer': 'Emma_North_Farmer'},
    {'SKU': 'v5', 'name': 'Onion', 'quantity': 442, 'validity': '24-08-30', 'farmer': 'Emma_North_Farmer'},
    {'SKU': 'v6', 'name': 'red onion', 'quantity': 231, 'validity': '24-08-21', 'farmer': 'Emma_North_Farmer'},
    {'SKU': 'v13', 'name': 'White cabbage', 'quantity': 327, 'validity': '24-09-30', 'farmer': 'Emma_North_Farmer'},
    {'SKU': 'v14', 'name': 'cauliflower', 'quantity': 482, 'validity': '24-09-12', 'farmer': 'Emma_North_Farmer'},
    {'SKU': 'v16', 'name': 'beet', 'quantity': 529, 'validity': '24-08-06', 'farmer': 'Emma_North_Farmer'},
    {'SKU': 'f14', 'name': 'strawberry', 'quantity': 234, 'validity': '24-08-17', 'farmer': 'Emma_North_Farmer'},
    {'SKU': 'v1', 'name': 'asparagus', 'quantity': 473, 'validity': '24-08-19', 'farmer': 'Emma_North_Farmer'},

    {'SKU': 'v10', 'name': 'Zucchini', 'quantity': 451, 'validity': '24-09-21', 'farmer': 'Evelyn_North_Farmer'},
    {'SKU': 'f2', 'name': 'Pear', 'quantity': 822, 'validity': '24-09-13', 'farmer': 'Evelyn_North_Farmer'},
    {'SKU': 'f11', 'name': 'Kiwi', 'quantity': 359, 'validity': '24-10-24', 'farmer': 'Evelyn_North_Farmer'},
    {'SKU': 'v7', 'name': 'Broccoli', 'quantity': 586, 'validity': '24-09-30', 'farmer': 'Evelyn_North_Farmer'},
    {'SKU': 'v11', 'name': 'Eggplant', 'quantity': 191, 'validity': '24-09-24', 'farmer': 'Evelyn_North_Farmer'},
    {'SKU': 'l5', 'name': 'Coriander', 'quantity': 351, 'validity': '24-10-03', 'farmer': 'Evelyn_North_Farmer'},
    {'SKU': 'v13', 'name': 'White cabbage', 'quantity': 143, 'validity': '24-09-22', 'farmer': 'Evelyn_North_Farmer'},
    {'SKU': 'v20', 'name': 'Hot Pepper', 'quantity': 217, 'validity': '24-09-05', 'farmer': 'Evelyn_North_Farmer'},
    {'SKU': 'v25', 'name': 'Squash', 'quantity': 196, 'validity': '24-09-11', 'farmer': 'Evelyn_North_Farmer'},
    {'SKU': 'f17', 'name': 'Hermon apple', 'quantity': 202, 'validity': '24-08-15', 'farmer': 'Evelyn_North_Farmer'},
    {'SKU': 'l1', 'name': 'Arugula', 'quantity': 180, 'validity': '24-08-29', 'farmer': 'Evelyn_North_Farmer'},
    {'SKU': 'l4', 'name': 'Champignon mushrooms', 'quantity': 239, 'validity': '24-10-01', 'farmer': 'Evelyn_North_Farmer'},


    {'SKU': 'v4', 'name': 'Sweet Potato', 'quantity': 363, 'validity': '24-10-25', 'farmer': 'Amelia_South_Farmer'},
    {'SKU': 'v10', 'name': 'Zucchini', 'quantity': 687, 'validity': '24-09-22', 'farmer': 'Amelia_South_Farmer'},
    {'SKU': 'v20', 'name': 'Hot Pepper', 'quantity': 490, 'validity': '24-09-17', 'farmer': 'Amelia_South_Farmer'},
    {'SKU': 'v25', 'name': 'Squash', 'quantity': 456, 'validity': '24-10-09', 'farmer': 'Amelia_South_Farmer'},
    {'SKU': 'v26', 'name': 'Garlic', 'quantity': 842, 'validity': '24-09-22', 'farmer': 'Amelia_South_Farmer'},
    {'SKU': 'l15', 'name': 'Thyme', 'quantity': 461, 'validity': '24-09-03', 'farmer': 'Amelia_South_Farmer'},
    {'SKU': 'f1', 'name': 'watermelon', 'quantity': 123, 'validity': '24-08-19', 'farmer': 'Amelia_South_Farmer'},
    {'SKU': 'f13', 'name': 'loquat', 'quantity': 214, 'validity': '24-09-10', 'farmer': 'Amelia_South_Farmer'},
    {'SKU': 'l3', 'name': "Caesar's hearts", 'quantity': 189, 'validity': '24-09-03', 'farmer': 'Amelia_South_Farmer'},
    {'SKU': 'l13', 'name': 'Round iceberg lettuce', 'quantity': 354, 'validity': '24-09-29', 'farmer': 'Amelia_South_Farmer'},
    {'SKU': 'l14', 'name': 'spinach', 'quantity': 473, 'validity': '24-10-01', 'farmer': 'Amelia_South_Farmer'},
    {'SKU': 'v9', 'name': 'pumpkin', 'quantity': 273, 'validity': '24-08-27', 'farmer': 'Amelia_South_Farmer'},
    {'SKU': 'v15', 'name': 'cucumber', 'quantity': 392, 'validity': '24-08-15', 'farmer': 'Amelia_South_Farmer'},

    {'SKU': 'f3', 'name': 'Blueberries', 'quantity': 578, 'validity': '24-08-01', 'farmer': 'Mateo_South_Farmer'},
    {'SKU': 'f4', 'name': 'Pineapple', 'quantity': 593, 'validity': '24-08-29', 'farmer': 'Mateo_South_Farmer'},
    {'SKU': 'f18', 'name': 'Jonathan Apple', 'quantity': 284, 'validity': '24-09-28', 'farmer': 'Mateo_South_Farmer'},
    {'SKU': 'f19', 'name': 'Pink Lady Apple', 'quantity': 803, 'validity': '24-09-24', 'farmer': 'Mateo_South_Farmer'},
    {'SKU': 'l10', 'name': 'Rocket', 'quantity': 679, 'validity': '24-08-06', 'farmer': 'Mateo_South_Farmer'},
    {'SKU': 'l11', 'name': 'Romaine Lettuce', 'quantity': 206, 'validity': '24-10-29', 'farmer': 'Mateo_South_Farmer'},
    {'SKU': 'v2', 'name': 'bean', 'quantity': 684, 'validity': '24-09-22', 'farmer': 'Mateo_South_Farmer'},
    {'SKU': 'f14', 'name': 'strawberry', 'quantity': 483, 'validity': '24-09-05', 'farmer': 'Mateo_South_Farmer'},
    {'SKU': 'l15', 'name': 'Thyme', 'quantity': 874, 'validity': '24-09-11', 'farmer': 'Mateo_South_Farmer'},
    {'SKU': 'f10', 'name': 'Pomelo', 'quantity': 382, 'validity': '24-08-15', 'farmer': 'Mateo_South_Farmer'},
    {'SKU': 'f5', 'name': 'peach', 'quantity': 323, 'validity': '24-08-29', 'farmer': 'Mateo_South_Farmer'},

    {'SKU': 'v1', 'name': 'Asparagus', 'quantity': 783, 'validity': '24-10-03', 'farmer': 'Benjamin_South_Farmer'},
    {'SKU': 'v7', 'name': 'Broccoli', 'quantity': 651, 'validity': '24-10-19', 'farmer': 'Benjamin_South_Farmer'},
    {'SKU': 'v12', 'name': 'Red Cabbage', 'quantity': 582, 'validity': '24-10-11', 'farmer': 'Benjamin_South_Farmer'},
    {'SKU': 'v15', 'name': 'Cucumber', 'quantity': 224, 'validity': '24-09-12', 'farmer': 'Benjamin_South_Farmer'},
    {'SKU': 'v16', 'name': 'Beet', 'quantity': 421, 'validity': '24-09-29', 'farmer': 'Benjamin_South_Farmer'},
    {'SKU': 'v24', 'name': 'Kolorbi', 'quantity': 819, 'validity': '24-09-11', 'farmer': 'Benjamin_South_Farmer'},
    {'SKU': 'f16', 'name': 'Grand Smith Apple', 'quantity': 304, 'validity': '24-10-08',
     'farmer': 'Benjamin_South_Farmer'},
    {'SKU': 'f17', 'name': 'Hermon Apple', 'quantity': 235, 'validity': '24-08-21', 'farmer': 'Benjamin_South_Farmer'},
        {'SKU': 'v8', 'name': 'carrot', 'quantity': 452, 'validity': '24-09-22', 'farmer': 'Benjamin_South_Farmer'},
    {'SKU': 'f15', 'name': 'orange', 'quantity': 307, 'validity': '24-09-05', 'farmer': 'Benjamin_South_Farmer'},
    {'SKU': 'v23', 'name': 'Yellow pepper', 'quantity': 518, 'validity': '24-09-11', 'farmer': 'Benjamin_South_Farmer'},
    {'SKU': 'f4', 'name': 'pineapple', 'quantity': 608, 'validity': '24-08-15', 'farmer': 'Benjamin_South_Farmer'},
    {'SKU': 'f18', 'name': 'Jonathan apple', 'quantity': 799, 'validity': '24-08-29', 'farmer': 'Benjamin_South_Farmer'},
    {'SKU': 'v17', 'name': 'tomato', 'quantity': 290, 'validity': '24-10-01', 'farmer': 'Benjamin_South_Farmer'},
    {'SKU': 'v27', 'name': 'corn', 'quantity': 754, 'validity': '24-09-15', 'farmer': 'Benjamin_South_Farmer'},

    {'SKU': 'v19', 'name': 'Red Pepper', 'quantity': 893, 'validity': '24-08-28', 'farmer': 'Levi_South_Farmer'},
    {'SKU': 'v20', 'name': 'Hot Pepper', 'quantity': 698, 'validity': '24-09-09', 'farmer': 'Levi_South_Farmer'},
    {'SKU': 'f8', 'name': 'Melon', 'quantity': 459, 'validity': '24-08-20', 'farmer': 'Levi_South_Farmer'},
    {'SKU': 'f9', 'name': 'Sabers', 'quantity': 680, 'validity': '24-10-06', 'farmer': 'Levi_South_Farmer'},
    {'SKU': 'l5', 'name': 'Coriander', 'quantity': 662, 'validity': '24-10-23', 'farmer': 'Levi_South_Farmer'},
    {'SKU': 'l13', 'name': 'Round Iceberg Lettuce', 'quantity': 653, 'validity': '24-09-17',
     'farmer': 'Levi_South_Farmer'},
    {'SKU': 'v5', 'name': 'Onion', 'quantity': 561, 'validity': '24-09-22', 'farmer': 'Levi_South_Farmer'},
    {'SKU': 'v6', 'name': 'red onion', 'quantity': 784, 'validity': '24-09-05', 'farmer': 'Levi_South_Farmer'},
    {'SKU': 'v13', 'name': 'White cabbage', 'quantity': 453, 'validity': '24-09-11', 'farmer': 'Levi_South_Farmer'},
    {'SKU': 'f2', 'name': 'pear', 'quantity': 690, 'validity': '24-08-15', 'farmer': 'Levi_South_Farmer'},
    {'SKU': 'f11', 'name': 'Kiwi', 'quantity': 512, 'validity': '24-08-29', 'farmer': 'Levi_South_Farmer'},
    {'SKU': 'l9', 'name': 'Portobello mushrooms', 'quantity': 638, 'validity': '24-10-01', 'farmer': 'Levi_South_Farmer'},

    {'SKU': 'f10', 'name': 'Pomelo', 'quantity': 746, 'validity': '24-10-07', 'farmer': 'Jack_South_Farmer'},
    {'SKU': 'v18', 'name': 'Cherry Tomato', 'quantity': 337, 'validity': '24-10-24', 'farmer': 'Jack_South_Farmer'},
    {'SKU': 'l14', 'name': 'Spinach', 'quantity': 536, 'validity': '24-09-29', 'farmer': 'Jack_South_Farmer'},
    {'SKU': 'f1', 'name': 'Watermelon', 'quantity': 445, 'validity': '24-09-13', 'farmer': 'Jack_South_Farmer'},
    {'SKU': 'f5', 'name': 'Peach', 'quantity': 558, 'validity': '24-10-28', 'farmer': 'Jack_South_Farmer'},
    {'SKU': 'l4', 'name': 'Champignon Mushroom', 'quantity': 485, 'validity': '24-09-03',
     'farmer': 'Jack_South_Farmer'},
    {'SKU': 'f9', 'name': 'Sabers', 'quantity': 560, 'validity': '2023-08-15', 'farmer': 'Jack_South_Farmer'},
    {'SKU': 'l5', 'name': 'Coriander', 'quantity': 350, 'validity': '2023-09-22', 'farmer': 'Jack_South_Farmer'},
    {'SKU': 'f12', 'name': 'clementine', 'quantity': 420, 'validity': '2023-10-05', 'farmer': 'Jack_South_Farmer'},
    {'SKU': 'v11', 'name': 'eggplant', 'quantity': 280, 'validity': '2023-08-30', 'farmer': 'Jack_South_Farmer'},
    {'SKU': 'v13', 'name': 'White cabbage', 'quantity': 650, 'validity': '2023-09-18', 'farmer': 'Jack_South_Farmer'},
    {'SKU': 'f20', 'name': 'lemon', 'quantity': 500, 'validity': '2023-10-12', 'farmer': 'Jack_South_Farmer'},
    {'SKU': 'l12', 'name': 'Rosemary', 'quantity': 390, 'validity': '2023-08-25', 'farmer': 'Jack_South_Farmer'},


    {'SKU': 'v4', 'name': 'Sweet Potato', 'quantity': 811, 'validity': '24-08-15', 'farmer': 'Ezra_Center_Farmer'},
    {'SKU': 'l1', 'name': 'Arugula', 'quantity': 511, 'validity': '24-10-18', 'farmer': 'Ezra_Center_Farmer'},
    {'SKU': 'l2', 'name': 'Bok Choi', 'quantity': 364, 'validity': '24-09-07', 'farmer': 'Ezra_Center_Farmer'},
    {'SKU': 'l7', 'name': 'Mint', 'quantity': 483, 'validity': '24-09-27', 'farmer': 'Ezra_Center_Farmer'},
    {'SKU': 'l6', 'name': 'Curled Lettuce', 'quantity': 698, 'validity': '24-10-20', 'farmer': 'Ezra_Center_Farmer'},
    {'SKU': 'v10', 'name': 'Zucchini', 'quantity': 306, 'validity': '24-08-16', 'farmer': 'Ezra_Center_Farmer'},
    {'SKU': 'v20', 'name': 'Hot Pepper', 'quantity': 138, 'validity': '24-08-03', 'farmer': 'Ezra_Center_Farmer'},
    {'SKU': 'f1', 'name': 'watermelon', 'quantity': 620, 'validity': '2023-09-05', 'farmer': 'Ezra_Center_Farmer'},
    {'SKU': 'f13', 'name': 'loquat', 'quantity': 270, 'validity': '2023-08-25', 'farmer': 'Ezra_Center_Farmer'},
    {'SKU': 'l3', 'name': "Caesar's hearts", 'quantity': 480, 'validity': '2023-10-12', 'farmer': 'Ezra_Center_Farmer'},
    {'SKU': 'l13', 'name': 'Round iceberg lettuce', 'quantity': 330, 'validity': '2023-09-18', 'farmer': 'Ezra_Center_Farmer'},
    {'SKU': 'l14', 'name': 'spinach', 'quantity': 710, 'validity': '2023-08-30', 'farmer': 'Ezra_Center_Farmer'},
    {'SKU': 'v9', 'name': 'pumpkin', 'quantity': 590, 'validity': '2023-10-03', 'farmer': 'Ezra_Center_Farmer'},
    {'SKU': 'v15', 'name': 'cucumber', 'quantity': 400, 'validity': '2023-08-15', 'farmer': 'Ezra_Center_Farmer'},

    {'SKU': 'f3', 'name': 'Blueberries', 'quantity': 816, 'validity': '24-08-17', 'farmer': 'Michael_Center_Farmer'},
    {'SKU': 'v16', 'name': 'Beet', 'quantity': 490, 'validity': '24-08-15', 'farmer': 'Michael_Center_Farmer'},
    {'SKU': 'l10', 'name': 'Rocket', 'quantity': 372, 'validity': '24-10-12', 'farmer': 'Michael_Center_Farmer'},
    {'SKU': 'v26', 'name': 'Garlic', 'quantity': 126, 'validity': '24-08-27', 'farmer': 'Michael_Center_Farmer'},
    {'SKU': 'l11', 'name': 'Romaine Lettuce', 'quantity': 617, 'validity': '24-08-12',
     'farmer': 'Michael_Center_Farmer'},
    {'SKU': 'v18', 'name': 'Cherry Tomato', 'quantity': 293, 'validity': '24-10-19', 'farmer': 'Michael_Center_Farmer'},
    {'SKU': 'v2', 'name': 'bean', 'quantity': 340, 'validity': '2023-09-08', 'farmer': 'Michael_Center_Farmer'},
    {'SKU': 'f14', 'name': 'strawberry', 'quantity': 500, 'validity': '2023-08-20', 'farmer': 'Michael_Center_Farmer'},
    {'SKU': 'l15', 'name': 'Thyme', 'quantity': 670, 'validity': '2023-10-10', 'farmer': 'Michael_Center_Farmer'},
    {'SKU': 'f10', 'name': 'Pomelo', 'quantity': 280, 'validity': '2023-09-15', 'farmer': 'Michael_Center_Farmer'},
    {'SKU': 'f5', 'name': 'peach', 'quantity': 430, 'validity': '2023-08-28', 'farmer': 'Michael_Center_Farmer'},

    {'SKU': 'v1', 'name': 'Asparagus', 'quantity': 293, 'validity': '24-10-21', 'farmer': 'Daniel_Center_Farmer'},
    {'SKU': 'v12', 'name': 'Red Cabbage', 'quantity': 513, 'validity': '24-09-14', 'farmer': 'Daniel_Center_Farmer'},
    {'SKU': 'v14', 'name': 'Cauliflower', 'quantity': 825, 'validity': '24-09-02', 'farmer': 'Daniel_Center_Farmer'},
    {'SKU': 'v22', 'name': 'Orange Pepper', 'quantity': 844, 'validity': '24-08-15', 'farmer': 'Daniel_Center_Farmer'},
    {'SKU': 'f19', 'name': 'Pink Lady Apple', 'quantity': 201, 'validity': '24-10-24',
     'farmer': 'Daniel_Center_Farmer'},
    {'SKU': 'v8', 'name': 'carrot', 'quantity': 610, 'validity': '2023-09-03', 'farmer': 'Daniel_Center_Farmer'},
    {'SKU': 'f15', 'name': 'orange', 'quantity': 290, 'validity': '2023-08-22', 'farmer': 'Daniel_Center_Farmer'},
    {'SKU': 'v23', 'name': 'Yellow pepper', 'quantity': 520, 'validity': '2023-10-08', 'farmer': 'Daniel_Center_Farmer'},
    {'SKU': 'f4', 'name': 'pineapple', 'quantity': 450, 'validity': '2023-09-18', 'farmer': 'Daniel_Center_Farmer'},
    {'SKU': 'f18', 'name': 'Jonathan apple', 'quantity': 360, 'validity': '2023-08-30', 'farmer': 'Daniel_Center_Farmer'},
    {'SKU': 'v17', 'name': 'tomato', 'quantity': 700, 'validity': '2023-09-15', 'farmer': 'Daniel_Center_Farmer'},
    {'SKU': 'v27', 'name': 'corn', 'quantity': 270, 'validity': '2023-08-25', 'farmer': 'Daniel_Center_Farmer'},

    {'SKU': 'v19', 'name': 'Red Pepper', 'quantity': 703, 'validity': '24-08-24', 'farmer': 'Samuel_Center_Farmer'},
    {'SKU': 'v28', 'name': 'Potato', 'quantity': 872, 'validity': '24-09-22', 'farmer': 'Samuel_Center_Farmer'},
    {'SKU': 'f7', 'name': 'Banana', 'quantity': 733, 'validity': '24-09-16', 'farmer': 'Samuel_Center_Farmer'},
    {'SKU': 'v14', 'name': 'Cauliflower', 'quantity': 368, 'validity': '24-09-02', 'farmer': 'Samuel_Center_Farmer'},
    {'SKU': 'f6', 'name': 'Grapefruit', 'quantity': 898, 'validity': '24-08-25', 'farmer': 'Samuel_Center_Farmer'},
    {'SKU': 'l8', 'name': 'Mushroom King of The Forest', 'quantity': 348, 'validity': '24-08-23',
     'farmer': 'Samuel_Center_Farmer'},
    {'SKU': 'v20', 'name': 'Hot Pepper', 'quantity': 834, 'validity': '24-10-07', 'farmer': 'Samuel_Center_Farmer'},
    {'SKU': 'f8', 'name': 'Melon', 'quantity': 242, 'validity': '24-08-17', 'farmer': 'Samuel_Center_Farmer'},
    {'SKU': 'v5', 'name': 'Onion', 'quantity': 530, 'validity': '2023-09-12', 'farmer': 'Samuel_Center_Farmer'},
    {'SKU': 'v6', 'name': 'red onion', 'quantity': 380, 'validity': '2023-08-28', 'farmer': 'Samuel_Center_Farmer'},
    {'SKU': 'v13', 'name': 'White cabbage', 'quantity': 650, 'validity': '2023-10-05', 'farmer': 'Samuel_Center_Farmer'},
    {'SKU': 'f2', 'name': 'pear', 'quantity': 420, 'validity': '2023-09-18', 'farmer': 'Samuel_Center_Farmer'},
    {'SKU': 'f11', 'name': 'Kiwi', 'quantity': 290, 'validity': '2023-08-22', 'farmer': 'Samuel_Center_Farmer'},
    {'SKU': 'l9', 'name': 'Portobello mushrooms', 'quantity': 550, 'validity': '2023-10-10', 'farmer': 'Samuel_Center_Farmer'},


    {'SKU': 'v3', 'name': 'Artichoke', 'quantity': 584, 'validity': '24-10-17', 'farmer': 'Alexander_Center_Farmer'},
    {'SKU': 'v7', 'name': 'Broccoli', 'quantity': 885, 'validity': '24-09-30', 'farmer': 'Alexander_Center_Farmer'},
    {'SKU': 'v24', 'name': 'Kolorbi', 'quantity': 631, 'validity': '24-08-08', 'farmer': 'Alexander_Center_Farmer'},
    {'SKU': 'f16', 'name': 'Grand Smith Apple', 'quantity': 217, 'validity': '24-08-31',
     'farmer': 'Alexander_Center_Farmer'},
    {'SKU': 'f17', 'name': 'Hermon Apple', 'quantity': 399, 'validity': '24-10-25',
     'farmer': 'Alexander_Center_Farmer'},
    {'SKU': 'l4', 'name': 'Champignon Mushroom', 'quantity': 665, 'validity': '24-10-11',
     'farmer': 'Alexander_Center_Farmer'},
    {'SKU': 'v25', 'name': 'Squash', 'quantity': 618, 'validity': '24-10-04', 'farmer': 'Alexander_Center_Farmer'},
    {'SKU': 'f9', 'name': 'Sabers', 'quantity': 420, 'validity': '2023-09-05', 'farmer': 'Alexander_Center_Farmer'},
    {'SKU': 'l5', 'name': 'Coriander', 'quantity': 590, 'validity': '2023-08-25', 'farmer': 'Alexander_Center_Farmer'},
    {'SKU': 'f12', 'name': 'clementine', 'quantity': 360, 'validity': '2023-10-08', 'farmer': 'Alexander_Center_Farmer'},
    {'SKU': 'v11', 'name': 'eggplant', 'quantity': 670, 'validity': '2023-09-15', 'farmer': 'Alexander_Center_Farmer'},
    {'SKU': 'v13', 'name': 'White cabbage', 'quantity': 480, 'validity': '2023-08-30', 'farmer': 'Alexander_Center_Farmer'},
    {'SKU': 'f20', 'name': 'lemon', 'quantity': 520, 'validity': '2023-10-03', 'farmer': 'Alexander_Center_Farmer'},
    {'SKU': 'l12', 'name': 'Rosemary', 'quantity': 330, 'validity': '2023-08-22', 'farmer': 'Alexander_Center_Farmer'}
    ]


def populate_products(app, db):
    with app.app_context():
        for product in products:
            product_record = db.session.query(Product).filter_by(sku=product['SKU'],
                                                                 farmer_id=farmersId[product['farmer']]).first()
            if not product_record:
                product_record = Product(sku=product['SKU'], name=product['name'], quantity=product['quantity'],
                                         validity=product['validity'], farmer_id=farmersId[product['farmer']])
                db.session.add(product_record)
        db.session.commit()


def populate_db(app, db):
    populate_product_details(app, db)
    populate_addresses(app, db)
    populate_users(app, db)
    populate_farmers(app, db)
    populate_deliverymen(app, db)
    populate_products(app, db)
