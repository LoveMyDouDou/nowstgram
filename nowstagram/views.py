#coding=utf-8

from nowstagram import app,db
from models import Image,User
from flask import render_template,redirect,request,flash,get_flashed_messages
import random,hashlib
from flask_login import login_user,logout_user,current_user,login_required

@app.route('/')
def index():
    images=Image.query.order_by('id desc').limit(10).all()
    return render_template('index.html',images=images)

@app.route('/image/<int:image_id>')
def image(image_id):
    image=Image.query.get(image_id)
    if image==None:
        return redirect('/')
    return render_template('pageDetail.html',image=image)

@app.route('/profile/<int:user_id>/')
@login_required
def profile(user_id):
    user=User.query.get(user_id)
    if user==None:
        return render_template('/')
    return render_template('profile.html',user=user)


@app.route('/regloginpage/')
def regloginpage():
    msg=''
    for m in get_flashed_messages(with_categories=False,category_filter=['reglogin']):
        msg=msg+m
    return render_template('login.html',msg=msg)


def redirect_with_msg(target,msg,category):
    if msg!=None:
        flash(msg,category=category)
    return redirect(target)

@app.route('/reg/',methods={'post','get'})
def reg():
    #request.args
    #request.form
    username=request.values.get('username').strip()
    password=request.values.get('password').strip()

    user=User.query.filter_by(username=username).first()

    if username=='' or password=='':
        return redirect_with_msg('/regloginpage/',u'用户名或密码不能为空',category='reglogin')

    if user!=None:
        return redirect_with_msg('/regloginpage/',u'用户名已经存在',category='reglogin')

    #更多判断

    salt='.'.join(random.sample('1234567890asdfghjklASDFGHJKL',10))
    m=hashlib.md5()
    m.update(password+salt)
    password=m.hexdigest()
    user =User(username,password,salt)
    db.session.add(user)
    db.session.commit()

    login_user(user)

    return redirect('/')

@app.route('/logout/')
def logout():
    login_user()
    return redirect('/')