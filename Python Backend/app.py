from flask import Flask, request, render_template, session, redirect, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy#, BaseQuery
import hashlib, random, math, #time, threading, json
from sqlalchemy import or_, and_
from datetime import date
#import requests

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
    interests = db.Column(db.VARCAHR(500), nullable=False) # interest1#interest2#
    base_location = db.Column(db.VARCHAR(500), nullable=False)
    base_lat = db.Column(db.Integer(), nullable=False)
    base_long = db.Column(db.Integer(), nullable=False)
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
    #barcode = db.Column(db.VARCHAR(25), primary_key=True) # id
    name = db.Column(db.VARCHAR(200), nullable=False)
    brand = db.Column(db.VARCHAR(100), nullable=False)
    #size = db.Column(db.VARCHAR(40), nullable=False)
    description = db.Column(db.VARCHAR(1000), nullable=False)
    mrp = db.Column(db.VARCHAR(10), nullable=False) # mrp in $
    seller = db.Column(db.VARCHAR(100), nullable=False) # Connect to Users..
    #total_quantity = db.Column(db.Integer(), nullable=False)
    img_addr = db.Column(db.VARCHAR(200), default='https://source.unsplash.com/random/300x200')
    location = db.Column(db.VARCHAR(1000), nullable=False)
    latitude = db.Column(db.Integer(), nullable=False)
    longitude = db.Column(db.Integer(), nullable=False)
    contact_info = db.Column(db.VARCHAR(1000), nullable=False) #Give Contact Info Here..
    #tags = db.Column(db.String(), nullable=False)
    def __repr__(self):
        return '(Task %r)' %self.id

class msgs(db.Model):###
    __tablename__ = "msgs"
    id = db.Column(db.Integer(), primary_key=True)
    sender = db.Column(db.VARCHAR(100), nullable=False)
    receiver = db.Column(db.VARCHAR(100), nullable=False)
    msg = db.Column(db.VARCHAR(10000), nullable=False)
    rd = db.Column(db.Boolean(), nullable=False, default=False)
    def __repr__(self):
        return '(Task %r)' %self.id

class walls(db.Model):
    __tablename__ = "walls"
    id = db.Column(db.Integer(), primary_key=True)
    owner = db.Column(db.VARCHAR(100), nullable=False)
    name = db.Column(db.VARCHAR(200), nullable=False, unique=True)
    base_location = db.Column(db.VARCHAR(300), nullable=False)
    base_lat = db.Column(db.Integer(), nullable=False)
    base_long = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.VARCHAR(500), nullable=False)

    def __repr__(self):
        return '(Task %r)' %self.id

class wallMsg(db.Model):
    __tablename__ = 'wallMsg'
    id = db.Column(db.Integer(), primary_key=True)
    wallId = db.Column(db.Integer(), nullable=False) # Corresponds to a Wall # ID
    msg = db.Column(db.VARCHAR(10000), nullable=False)
    sender = db.Column(db.VARCHAR(100), nullable=False)
    def __repr__(self):
        return '(task %r)' %self.id

class events(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer(), primary_key=True)
    owner = db.Column(db.VARCHAR(100), nullable=False)
    name = db.Column(db.VARCHAR(500), nullable=False)
    description = db.Column(db.VARCHAR(1000), nullable=False)
    date = db.Column(db.VARCHAR(10), nullable=False)
    time = db.Column(db.VARCHAR(8), nullable=False)
    time_zone = db.Column(db.VARCHAR(10), nullable=False)
    wall = db.Column(db.Integer(), nullable=False) # Connected To A Wall
    location = db.Column(db.VARCHAR(500), nullable=False)
    lat = db.Column(db.Integer(), nullable=False)
    long = db.Column(db.Integer(), nullable=False)
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
        interests = request.form['interests']
        base_location = request.form['base_location']
        base_lat = request.form['base_lat']
        base_long = request.form['base_log']
        user_check = users.query.get(email_address)
        if user_check:
            return jsonify({'conf': 1})
        else:
            add = users(email_address=email_address, name=name, interests=interests,base_location=base_location, base_lat=base_lat, base_long=base_long, password=hashlib.sha256(password.encode()).hexdigest())
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
        seller = request.form['seller']
        img_addr = request.form['img_addr']
        location = request.form['location']
        lat = request.form['lat']
        long = request.form['long']
        contact_info = request.form['contact_info']
        #AUTH
        seller = user_validation(doa, random_key)
        if seller != 'False':
            add = items(name=name, description=description, brand=brand, mrp=mrp, seller=seller, img_addr=img_addr, location=location, latitude=lat, longitude=long, contact_info=contact_info)
            db.session.add(add)
            db.session.commit()
            return jsonify({'conf': 0})
        else:
            return jsonify({'conf': 1})

@app.route('/api/get/item', methods=['POST'])
def get_item_api():
    if request.method == 'POST':
        id = request.form['id']
        item = items.query.get(id)
        if item:
            return jsonify({'conf': 0, 'name': item.name, 'brand': item.brand, 'description': item.description, 'mrp': item.mrp, "seller": item.seller, 'img_addr': item.img_addr, 'location': item.location, 'lat': item.lat, 'long': item.long, 'contact_info': item.contact_info})
        else:
            return jsonify({'conf': 1})

@app.route('/api/send/msg', methods=['POST'])
def send_msg_api():
    if request.method == 'POST':
        random_key = request.form['random_key']
        doa = request.form['doa']
        sender = user_validation(doa, random_key)
        receiver = request.form['receiver']
        msg = request.form['msg']
        #sender AUTH
        if sender != 'False':
            add = msgs(sender=sender, receiver=receiver, msg=msg)
            db.session.add(add)
            db.session.commit()
            return jsonify({'conf': 0})
        else:
            return jsonify({'conf': 1})

@app.route('/api/get/dm', methods=['POST'])###
def get_msgs_api():
    if request.method == 'POST':
        random_key = request.form['random_key']
        doa = request.form['doa']
        receiver = user_validation(doa, random_key)
        sender = request.form['sender']
        # receiver AUTH
        if receiver != 'False':
            msgs.query.filter(and_(msgs.sender==sender, msgs.receiver==receiver)).all()
            send_data = []
            n = 0
            for msg in msgs:
                n +=1
                send_data.append({'id': msg.id, 'msg': msg})
            return jsonify({'conf': 0, 'data': send_data, 'number_of_msgs': n})
        else:
            return jsonify({'conf': 1})

@app.route('/api/create/wall', methods=['POST'])
def create_wall_api():
    if request.method == 'POST':
        random_key = request.form['random_key']
        doa = request.form['doa']
        owner = user_validation(doa, random_key)
        name = request.form['name']
        base_location = request.form['base_location']
        base_lat = request.form['base_lat']
        base_long = request.form['base_long']
        description = request.form['description']
        #Owner AUTH
        if owner != 'False':
            add = walls(owner=owner, name=name, base_location=base_location, base_lat=base_lat, base_long=base_long, description=description)
            db.session.add(add)
            db.session.commit()
            return jsonify({'conf': 0})
        else:
            return jsonify({'conf':1})

@app.route('/api/send/wallMsg', methods=['POST'])
def send_wall_msg_api():
    if request.method == 'POST':
        wallId = int(request.form['wallId'])
        msg = request.form['msg']
        random_key = request.form['random_key']
        doa = request.form['doa']
        sender = user_validation(doa, random_key)
        #Sender AUTH
        if sender != 'False':
            add = wallMsg(wallId=wallId, msg=msg, sender=sender)
            db.session.add(add)
            db.session.commit()
            return jsonify({'conf':0})
        else:
            return jsonify({'conf': 1})

@app.route('/api/get/wallMsgs', methods=['POST'])
def get_wall_msgs_api():
    if request.method == "POST":
        wallId = int(request.form['wallId'])
        wall = walls.query.get(wallId)
        if wall:
            wallMsgs = wallMsg.query.filter_by(wallId=wallId).all()
            send_data = []
            n = 0
            for msg in wallMsgs:
                n += 1
                send_data.append({'id': msg.id, 'sender': msg.sender, 'msg': msg.msg})
            return jsonify({'conf': 0, 'data': send_data, 'number': n})
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
        time_zone = request.form['time_zone']
        wall = request.form['wall']
        location = request.form['location']
        lat = request.form['lat']
        long = request.form['long']
        #Owner AUTH
        if owner != 'False':
            add = events(owner=owner, name=name, description=description, date=date, time=time, time_zone=time_zone, wall=wall, location=location, lat=lat, long=long)
            db.session.add(add)
            db.session.commit()
            return jsonify({'conf': 0})
        else:
            return jsonify({'conf': 1})

@app.route('/api/get/msgs/new', methods=['POST'])
def get_msgs_new_api():
    if request.method == 'POST':
        sender = request.form['sender']
        random_key = request.form['random_key']
        doa = request.form['doa']
        receiver = user_validation(doa, random_key)
        #receiver = request.form['receiver']
        #Receiver AUTH
        if receiver != 'False':
            msgs.query.filter(and_(msgs.sender==sender, msgs.receiver==receiver, msgs.rd==False)).all()
            send_data = []
            n = 0
            for msg in msgs:
                n +=1
                msgs.query.get(msg.id).rd = True
                db.session.commit()
                send_data.append({'id': msg.id, 'msg': msg})
            return jsonify({'conf': 0, 'data': send_data, 'number_of_msgs': n})
        else:
            return jsonify({'conf': 1})

@app.route('/api/event/signup', methods=['POST'])
def event_signup_api():
    if request.method == 'POST':
        random_key = request.form['random_key']
        doa = request.form['doa']
        user = user_validation(doa, random_key)
        event_id = request.form['event_id']
        if user != 'False':
            add = signups(user=user, event_id=event_id)
            db.session.add(add)
            db.session.commit()
            return jsonify({'conf': 0})
        else:
            return jsonify({'conf': 1})


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, threaded=True, debug=True)
