from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
#from django.utils import TIME_ZONE
#from django.views.generics import DetailView, ListView, UpdateView
#from carnisseria.models import Botiga, Carns
#from carnisseria.forms import BotigaForm, CarnsForn
#from carnisseria.views import BotigaCreate, CarnsCreate, BotigaDetail

urlpatterns = [
    # Restaurant details, ex.: /myrestaurants/restaurants/1/
    path('', views.homepage, name='homepage'),
    path('carns/', views.carns, name='carns'),
    path('precuinats/', views.precuinats, name='precuinats'),
]
