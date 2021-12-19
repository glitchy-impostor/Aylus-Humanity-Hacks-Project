from flask import Flask, request, render_template, session, redirect, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy#, BaseQuery
import hashlib, random, math, time, threading, json
from sqlalchemy import or_, and_
from datetime import date
import requests

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://aylushacksprj:aylusTeam1234@aylushacksprj.mysql.pythonanywhere-services.com/aylushacksprj$aylusDB1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] = 'dcvbhjuygfvbnjm,.hnbvcxswdfdertgfvbnnjhgbvfcerty67654324567uhbvcxz'

class users(db.Model):
    __tablename__ = "users"
    email_address = db.Column(db.VARCHAR(128), primary_key=True)
    password = db.Column(db.VARCAHR(1000), nullable=False)
    name = db.Column(db.VARCAHR(100), nullable=False)
    points = db.Column(db.Integer(), nullable=False)
    def __repr__(self):
        return '<Task %r>' %self.id

class currentLogins(db.Model):
    __tablename__ = "currentLogins"
    random_key = db.Column(db.VARCAHR(10), primary_key=True)
    doa = db.Column(db.VARCHAR(10), nullable=False)
    email_address = db.Column(db.VARCHAR(128), nullable=False)
    def __repr__(self):
        return '<Task %s>' %self.id

class items(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.VARCHAR(200), nullable=False)
    brand = db.Column(db.VARCHAR(100), nullable=False)
    description = db.Column(db.VARCHAR(1000), nullable=False)
    mrp = db.Column(db.VARCHAR(10), nullable=False) # mrp in $
    seller = db.Column(db.VARCHAR(100), nullable=False) # Connect to Users..
    location = db.Column(db.VARCHAR(1000), nullable=False)
    latitudeH = db.Column(db.VARCHAR(20), nullable=False)
    longitudeH = db.Column(db.VARCHAR(20), nullable=False)
    latitudeB = db.Column(db.VARCHAR(20), nullable=False)
    longitudeB = db.Column(db.VARCHAR(20), nullable=False)
    contact_info = db.Column(db.VARCHAR(1000), nullable=False) #Give Contact Info Here..
    #tags = db.Column(db.String(), nullable=False)
    def __repr__(self):
        return '(Task %r)' %self.id

class r_items(db.Model):
    __tablename__ = 'r_items'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.VARCHAR(200), nullable=False)
    description = db.Column(db.VARCHAR(500), nullable=False)
    location = db.Column(db.VARCHAR(1000), nullable=False)
    latitudeH = db.Column(db.VARCHAR(20), nullable=False)
    longitudeH = db.Column(db.VARCHAR(20), nullable=False)
    latitudeB = db.Column(db.VARCHAR(20), nullable=False)
    longitudeB = db.Column(db.VARCHAR(20), nullable=False)
    contact_info = db.Column(db.VARCHAR(1000), nullable=False) #Give Contact Info Here..
    user = db.Column(db.VARCHAR(100), nullable=False)
    def __repr__(self):
        return '<Task %s>' %self.id

class events(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer(), primary_key=True)
    owner = db.Column(db.VARCHAR(100), nullable=False)
    name = db.Column(db.VARCHAR(500), nullable=False)
    description = db.Column(db.VARCHAR(1000), nullable=False)
    date = db.Column(db.VARCHAR(10), nullable=False)
    time = db.Column(db.VARCHAR(8), nullable=False)
    location = db.Column(db.VARCHAR(500), nullable=False)
    latH = db.Column(db.VARCHAR(20), nullable=False)
    longH = db.Column(db.VARCHAR(20), nullable=False)
    latB = db.Column(db.VARCHAR(20), nullable=False)
    longB = db.Column(db.VARCHAR(20), nullable=False)
    def __repr__(self):
        return '(Task %r)' %self.id

class signups(db.Model):
    __tablename__ = 'signups'
    id = db.Column(db.Integer(), primary_key=True)
    user = db.Column(db.VARCHAR(100), nullable=False)
    event_id = db.Column(db.Integer(), nullable=False) # Connects to Enent ID
    def __repr__(self):
        return '<Task %r>' %self.id

'''Common python functions'''

def create_uid():
    chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    random.shuffle(chars)
    r = ''
    for x in range(10):
        r += chars[random.randint(0, 35)]
    return r

def user_validation(doa, random_key):
    validate_user = currentLogins.query.get(random_key)
    if validate_user:
        if validate_user.date_of_addition == doa: return validate_user.email_address
        else: return 'False'
    else: return 'False'

@app.route('/')
def index():
    return 'HI'

@app.route('/api/login', methods=['POST'])
def login_api():
    if request.method == 'POST':
        email_address = request.form['email_address']
        password = request.form['password']
        hashed_pass = hashlib.sha256(password.encode()).hexdigest()
        user = users.query.get(email_address)
        if user:
            if user.password == hashed_pass:
                uid = create_uid()
                doa = str(date.today())
                add = currentLogins(random_key=uid, doa=doa, email_address=email_address)
                db.session.add(add)
                db.session.commit()
                return jsonify({'conf': 0, 'random_key': uid, 'doa': doa})
            else:
                return jsonify({'conf': 1})
        else:
            return jsonify({'conf': 2})

@app.route('/api/signup', methods=['POST'])
def signup_api():
    if request.method == 'POST':
        email_address = request.form['email_address']
        password = request.form['password']
        name = request.form['name']
        if user_check:
            return jsonify({'conf': 1})
        else:
            add = users(email_address=email_address, name=name, password=hashlib.sha256(password.encode()).hexdigest(), points=0)
            db.session.add(add)
            uid = create_uid()
            doa = str(date.today())
            addition = currentLogins(random_key=uid, doa=doa, email_address=email_address)
            db.session.add(addition)
            db.session.commit()
            return jsonify({'conf': 0, 'random_key': uid, 'doa': doa})


@app.route('/api/add/items', methods=['POST'])
def add_items_api():
    if request.method == 'POST':
        name = request.form['name']
        brand = request.form['brand']
        description = request.form['description']
        mrp = request.form['mrp']
        random_key = request.form['random_key']
        doa = request.form['doa']
        location = request.form['location']
        r = requests.get('https://nominatim.openstreetmap.org/search.php?q='+location+'&polygon_geojson=1&limit=50&format=json')
        long = r.json()[0]['lon']
        lat = r.json()[0]['lat']
        latH = lat.split('.')[0]
        longH = long.split('.')[0]
        latB = lat.split('.')[1]
        longB = lat.split('.')[1]
        condition = int(request.form['condition'])
        contact_info = request.form['contact_info']
        #AUTH
        seller = user_validation(doa, random_key)
        if seller != 'False':
            if condition == 0:
                add = items(name=name, description=description, brand=brand, mrp=mrp, seller=seller, location=location, latitudeH=latH, longitudeH=longH,latitudeB=latB,longitudeB=latB, contact_info=contact_info)
                db.session.add(add)
                user = users.query.get(seller)
                user.points += 2
                db.session.commit()
                return jsonify({'conf': 0})
            else:
                add = r_items(name=name, description=description, location=location, latitudeH=latH, latitudeB=latB, longitudeH=longH, longitudeB=longB, contact_info=contact_info, user=seller)
                db.session.add(add)
                user = users.query.get(seller)
                user.points += 2
                db.session.commit()
                return jsonify({'conf': 5})
        else:
            return jsonify({'conf': 1})

@app.route('/api/get/item', methods=['POST'])
def get_item_api():
    if request.method == 'POST':
        id = int(request.form['id'])
        item = items.query.get(id)
        if item:
            seller = users.query.get(item.seller)
            return jsonify({'conf': 0, 'name': item.name, 'brand': item.brand, 'description': item.description, 'mrp': item.mrp, "seller": item.seller, 'seller_name': seller.name, 'location': item.location, 'lat': item.latitudeH + '.' + item.latitudeB, 'long': item.longitudeH + '.' + item.longitudeB, 'contact_info': item.contact_info})
        else:
            return jsonify({'conf': 1})

@app.route('/api/create/event', methods=['POST'])
def create_event_api():
    if request.method == 'POST':
        random_key = request.form['random_key']
        doa = request.form['doa']
        owner = user_validation(doa, random_key)
        #owner = request.form['owner']
        name = request.form['name']
        description = request.form['description']
        date = request.form['date']
        time = request.form['time']
        location = request.form['location']
        r = requests.get('https://nominatim.openstreetmap.org/search.php?q='+location+'&polygon_geojson=1&limit=50&format=json')
        long = r.json()[0]['lon']
        lat = r.json()[0]['lat']
        latH = lat.split('.')[0]
        longH = long.split('.')[0]
        latB = lat.split('.')[1]
        longB = long.split('.')[1]
        #Owner AUTH
        if owner != 'False':
            add = events(owner=owner, name=name, description=description, date=date, time=time, location=location, latH=latH, longH=longH, latB=latB, longB=longB)
            db.session.add(add)
            user = users.query.get(owner)
            user.points += 10
            db.session.commit()
            return jsonify({'conf': 0})
        else:
            return jsonify({'conf': 1})

@app.route('/api/event/signup', methods=['POST'])
def event_signup_api():
    if request.method == 'POST':
        random_key = request.form['random_key']
        doa = request.form['doa']
        user = user_validation(doa, random_key)
        event_id = int(request.form['event_id'])
        if user != 'False':
            add = signups(user=user, event_id=event_id)
            db.session.add(add)
            userA = users.query.get(user)
            userA.points += 5
            db.session.commit()
            return jsonify({'conf': 0})
        else:
            return jsonify({'conf': 1})

@app.route('/api/search/events', methods=['POST'])
def search_events_api():
    if request.method == 'POST':
        cityName = request.form['city_name']
        r = requests.get('https://nominatim.openstreetmap.org/search.php?q='+cityName+'&polygon_geojson=1&limit=50&format=json')
        latUp = r.json()[0]['boundingbox'][1]
        latDown = r.json()[0]['boundingbox'][0]
        longUp = r.json()[0]['boundingbox'][2]
        longDown = r.json()[0]['boundingbox'][3]
        latUpH = latUp.split('.')[0]
        latUpB = latUp.split('.')[1]
        latDownH = latDown.split('.')[0]
        latDownB = latDown.split('.')[1]
        longUpH = longUp.split('.')[0]
        longUpB = longUp.split('.')[1]
        longDownH = longDown.split('.')[0]
        longDownB = longDown.split('.')[1]
        eventList = events.query.filter(and_(or_(events.latH == latUpH, events.latH == latDownH)), or_(events.longH == longUpH, events.longH==longDownH)).all()
        act_list = []
        for event in eventList:
            if (int(event.latB) >= int(latDownB) and int(event.latB) <= int(latUpB)) and (int(event.longB) >= int(longDownB) and int(event.longB) <= int(longUpB)):
                wall = walls.query.get(event.wall)
                user = users.query.get(event.owner)
                act_list.append({'id': event.id, 'name': event.name, 'description': event.description,'organiser':users.name , 'date': event.date, 'time':event.time, 'time_zone': event.time_zone, 'wall': event.wall,"wall_name": wall.name, 'location': event.location, 'latitude': (event.latH + '.' + event.latB),'longitude': (event.longH + '.' + event.longB) })
        return jsonify({'conf': 0, 'data': act_list})

@app.route('/api/edit/event', methods=['POST'])
def edit_event_api():
    id = int(request.form['id'])
    name = request.form['name']
    description = request.form['description']
    date = request.form['date']
    time = request.form['time']
    location = request.form['location']
    r = requests.get('https://nominatim.openstreetmap.org/search.php?q='+location+'&polygon_geojson=1&limit=50&format=json')
    long = r.json()[0]['lon']
    lat = r.json()[0]['lat']
    latH = lat.split('.')[0]
    latB = lat.split('.')[1]
    longH = long.split('.')[0]
    longB = long.split('.')[1]
    random_key = request.form['random_key']
    doa = request.form['doa']
    user = user_validation(doa, random_key)
    if user!='False':
        event = events.query.get(id)
        if event.owner == user:
            event.name = name
            event.description = description
            event.date = date
            event.time = time
            event.location = location
            event.latH = latH
            event.latB = latB
            event.longH = longH
            event.longB = longB
            db.session.commit()
            return jsonify({'conf': 0})
        else:
            return jsonify({'conf': 1})
    else:
        return jsonify({'conf': 2})

'''@app.route('/api/add/r-item', methods=['POST'])
def add_r_item_api():
    name = reuquest.form['name']
    brand = reuquest.form['brand']
    description = reuquest.form['description']
    condition = int(reuquest.form['condition'])
    location = reuquest.form['location']
    lat = reuquest.form['lat']
    long = reuquest.form['long']
    random_key = reuquest.form['random_key']
    doa = reuquest.form['doa']
    contact_info = reuquest.form['contact_info']
    user = user_validation(doa, random_key)
    if user!='False':
        add = r_items(name=name, brand=brand, description=description, condition=condition, location=location, contact_info=contact_info, user=user, latitudeH=lat.split('.')[0], latitudeB=lat.split('.')[1], longitudeH=long.split('.')[0], longitudeB=long.split('.')[1])
        db.session.add(add)
        db.session.commit()
        return jsonify({'conf': 0})
    return jsonify({'conf': 1})'''

@app.route('/api/get/r-item', methods=['POST'])
def get_r_item_api():
    id = int(request.form['id'])
    r_item = r_items.query.get(id)
    if r_item:
        user = users.query.get(r_item.user)
        data = {'id': r_item.id, 'name': r_item.name, 'brand': r_item.brand, 'description': r_item.description, 'condition': r_item.condition, 'location': r_item.location, 'latitude': (r_item.latitudeH + '.' + r_item.latitudeB), 'longitude': (r_item.longitudeH+'.'+r_item.longitudeB), 'contact_info': r_item.contact_info, 'user_name': user.name}
        return jsonify({'conf': 0, 'data': data})
    else:
        return jsonify({'conf': 1})

@app.route('/api/edit/r-item', methods=['POST'])
def edit_r_item_api():
    id = int(request.form['id'])
    name = reuquest.form['name']
    brand = reuquest.form['brand']
    description = reuquest.form['description']
    condition = int(reuquest.form['condition'])
    location = reuquest.form['location']
    lat = reuquest.form['lat']
    long = reuquest.form['long']
    random_key = reuquest.form['random_key']
    doa = reuquest.form['doa']
    contact_info = reuquest.form['contact_info']
    user = user_validation(doa, random_key)
    if user!='False':
        r_item = r_items.query.get(id)
        if r_item.user == user:
            r_item.name = name
            r_item.brand = brand
            r_item.description = description
            r_item.condition = condition
            r_item.location = location
            r_item.contact_info = contact_info
            r_item.latitudeH = lat.split('.')[0]
            r_item.latitudeB = lat.split('.')[1]
            r_item.longitudeH = long.split('.')[0]
            r_item.longitudeB = long.split('.')[1]
            db.session.commit()
            return jsonify({'conf': 0})
        else:
            return jsonify({'conf':1})
    return jsonify({'conf': 2})

@app.route('/api/delete/event', methods=['POST'])
def delete_event_api():
    id = int(request.form['id'])
    event = events.query.get(id)
    random_key = reuquest.form['random_key']
    doa = reuquest.form['doa']
    user = user_validation(doa, random_key)
    if event:
        if user!='False' and event.owner == user:
            db.session.delete(event)
            db.session.commit()
            return jsonify({'conf': 0})
        return jsonify({'conf': 1})
    return jsonify({'conf': 2})

@app.route('/api/delete/item', methods=['POST'])
def delete_item_api():
    id = int(request.form['id'])
    item = items.query.get(id)
    random_key = reuquest.form['random_key']
    doa = reuquest.form['doa']
    user = user_validation(doa, random_key)
    if item:
        if user!='False' and item.seller == user:
            db.session.delete(item)
            db.session.commit()
            return jsonify({'conf': 0})
        return jsonify({'conf': 1})
    return jsonify({'conf': 2})

@app.route('/api/delete/r-item', methods=['POST'])
def delete_r_item_api():
    id = int(request.form['id'])
    r_item = r_items.query.get(id)
    random_key = reuquest.form['random_key']
    doa = reuquest.form['doa']
    user = user_validation(doa, random_key)
    if r_item:
        if user!='False' and r_item.seller == user:
            db.session.delete(r_item)
            db.session.commit()
            return jsonify({'conf': 0})
        return jsonify({'conf': 1})
    return jsonify({'conf': 2})

@app.route('/api/get/leaderboard', methods=['GET'])
def get_leaderboard_api():
    dataR = users.query.order_by(users.points.desc()).limit(10)
    data = []
    n = 0
    for user in dataR:
        n += 1
        data.append({'email': user.email_address, 'name': user.name, 'points': user.points})
    return jsonify({'conf': 0, 'data': data, 'n': n})
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, threaded=True, debug=True)
