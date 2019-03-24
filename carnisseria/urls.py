from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from django.utils import TIME_ZONE
from django.views.generics import DetailView, ListView, UpdateView
from carnisseria.models import Botiga, Carns
from carnisseria.forms import BotigaForm, CarnsForn
from carnisseria.views import BotigaCreate, CarnsCreate, BotigaDetail

urlpatterns = [
    # Restaurant details, ex.: /myrestaurants/restaurants/1/
    url(r'^carnisseria/(?P<pk>\d+)/$',
        BotigaDetail.as_view(),
        name='botiga_detail'),

    # Restaurant carns details, ex: /myrestaurants/restaurants/1/dishes/1/
    url(r'^carnisseria/(?P<pkr>\d+)/carns/(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Carns,
            template_name='carnisseria/carns_detail.html'),
            name='carns_detail'),

    # Create a restaurant, /myrestaurants/restaurants/create/
    url(r'^restaurants/create/$',
        BotigaCreate.as_view(),
        name='botiga_create'),

    # Create a restaurant dish, ex.: /myrestaurants/restaurants/1/dishes/create/
    url(r'^restaurants/(?P<pk>\d+)/carns/create/$',
        CarnsCreate.as_view(),
        name='carns_create'),

]
