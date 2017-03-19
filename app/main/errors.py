'''
Created on 2017年3月19日

@author: chaohu
'''
from flask.templating import render_template
from . import main

@main.errorhandler(404)
def page_not_found(e):
    return render_template("error/404.html")

@main.errorhandler(500)
def internal_server_error(e):
    return render_template("error/500.html")
