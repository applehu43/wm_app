from django.shortcuts import render
from django.template import loader
from django.template.context import Context
from django.http.response import HttpResponse

# Create your views here.
def index(req):
#     posts = weight_rcd.objects.all()
#     t = loader.get_template("archive.html")
#     c = Context({'posts':posts})
    return HttpResponse('''<h2>really???</h2>''')