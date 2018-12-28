from models import BaseModel
from application import db


class Member(BaseModel, db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    mobile = db.Column(db.String(11), unique=True)
    nickName = db.Column(db.String(50), nullable=False, default='')
    gender = db.Column(db.SmallInteger, default=0)
    avatarUrl = db.Column(db.String(255))
    country = db.Column(db.String(50))
    province = db.Column(db.String(50))
    city = db.Column(db.String(50))
    salt = db.Column(db.String(255), nullable=False, default='')
    reg_id = db.Column(db.String(16), nullable=True)
    status = db.Column(db.SMALLINT, default=0)
