#coding=utf-8

from nowstagram import db
import random


class Image(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    url=db.Column(db.String(512))
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    create_date=db.Column(db.DateTime)

    def __init__(self,url,user):


class User(db.Model):
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(80),unique=True)
    password=db.Column(db.String(32))
    head_url=db.Column(db.String(256))

    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.head_url='http://images.nowcoder.com/head/'+str(random.randint(0,1000))+'m.png'

    def __repr__(self):
        return '<User %d %s>' %(self.id,self.username)