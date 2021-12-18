from flask import Flask, request, render_template, session, redirect, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy#, BaseQuery
#import random, math, time, threading, json
from sqlalchemy import or_, and_
#from datetime import date

app = Flask(__name__)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://aylushacksprj:aylusTeam1234@aylushacksprj.mysql.pythonanywhere-services.com/aylushacksprj$aylusDB1'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SECRET_KEY'] = 'dcvbhjuygfvbnjm,.hnbvcxswdfdertgfvbnnjhgbvfcerty67654324567uhbvcxz'

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

@app.route('/')
def index():
    return 'HI'

@app.route('/api/add/items', methods=['POST'])
def add_items_api():
    if request.method == 'POST':
        name = request.form['name']
        brand = request.form['brand']
        description = request.form['description']
        mrp = request.form['mrp']
        seller = request.form['seller']
        img_addr = request.form['img_addr']
        location = request.form['location']
        lat = request.form['lat']
        long = request.form['long']
        contact_info = request.form['contact_info']
        #AUTH
        if True:
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
        sender = request.form['sender']
        receiver = request.form['receiver']
        msg = request.form['msg']
        #sender AUTH
        if True:
            add = msgs(sender=sender, receiver=receiver, msg=msg)
            db.session.add(add)
            db.session.commit()
            return jsonify({'conf': 0})
        else:
            return jsonify({'conf': 1})

@app.route('/api/get/dm', methods=['POST'])###
def get_msgs_api():
    if request.method == 'POST':
        receiver = request.form['receiver']
        sender = request.form['sender']
        # receiver AUTH
        if True:
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
        owner = request.form['owner']
        name = request.form['name']
        base_location = request.form['base_location']
        base_lat = request.form['base_lat']
        base_long = request.form['base_long']
        description = request.form['description']
        #Owner AUTH
        if True:
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
        sender = request.form['sender']
        #Sender AUTH
        if True:
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
        owner = request.form['owner']
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
        if True:
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
        receiver = request.form['receiver']
        #Receiver AUTH
        if True:
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

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8080, threaded=True, debug=True)
