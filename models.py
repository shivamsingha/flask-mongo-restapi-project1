import datetime

from flask_mongoengine import MongoEngine

db = MongoEngine()


class AddressBook(db.Document):
    name = db.StringField(max_length=60)
    address = db.StringField(max_length=60)
    city = db.StringField(max_length=60)
    state = db.StringField(max_length=60)
    country = db.StringField(max_length=60)
    pincode=db.IntField()
    phone=db.StringField(max_length=13)
    email = db.StringField(max_length=60)
