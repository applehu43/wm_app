from django.template import loader
from django.http.response import HttpResponse
from wm_app.models import WeightRcd

# Create your views here.
def index(req):
    user_list = WeightRcd.objects.all()[:2]
    template = loader.get_template("webapp/index.html")
    context = {
        'user_list':user_list
    }
    return HttpResponse(template.render(context,req))

def detail(req,user_id):
    resp = "the user is: %s"
    return HttpResponse(resp % user_id)