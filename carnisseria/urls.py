from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from django.utils import TIME_ZONE
from django.views.generics import DetailView, ListView, UpdateView
from carnisseria.models import Botiga, Carns
from carnisseria.forms import BotigaForm, CarnsForn
from carnisseria.views import BotigaCreate, CarnsCreate, botiga_detail

urlpatterns = [
    #List latest 5 carns:

]
