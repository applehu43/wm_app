'''
Created on 2017年3月19日

@author: chaohu
'''
from flask.globals import request, session
from flask.helpers import make_response, url_for, flash
from werkzeug.utils import redirect
from flask_wtf.form import Form
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import Required
from flask.templating import render_template
from . import main
from app.migrations.models import UserInfo

@main.route("/")
def index():
#     user_agent = request.headers.get("User-Agent")
#     resp = make_response("<h4>test flask in '%s'</h4>" % user_agent)
    name = session['name']
    return render_template('index.html',name=name)

@main.route("/wm/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        name = session['name'] =form.name.data
#         user = UserInfo.query(name).first()
        user = None
        password = form.password.data
#         if user is not None and user.password == password:
        if True:
            return redirect(url_for('main.index'))
        flash('密码错误')
    return render_template('login.html', form=form,
                           name=session.get('name'))
@main.route("/wm/logout", methods=['GET', 'POST'])
def logout():
    flash('you have been logged out')
    session['name'] = None
    return redirect(url_for('main.index'))
    
class LoginForm(Form):
    name = StringField('帐号：', validators=[Required()])
    password = PasswordField('密码：', validators=[Required()])
    submit = SubmitField("登录")
