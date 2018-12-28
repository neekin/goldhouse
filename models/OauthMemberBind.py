from models import BaseModel
from application import db


class OauthMemberBind(BaseModel, db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    member_id = db.Column(db.INTEGER, nullable=False, default=0)
    client_type = db.Column(db.String(20), nullable=False, default='')
    type = db.Column(db.SmallInteger, nullable=False, default=0)
    openid = db.Column(db.String(80), nullable=False, default='')
    unionid = db.Column(db.String(100), nullable=False, default='')
