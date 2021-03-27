from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('get_all_data', views.get_all_data, name='fetch all'),
    path('getDistinctValue', views.getDistinctValue, name="fetch Year range"),
    path('getVaccinationForTwoLocation', csrf_exempt(views.getVaccinationForTwoLocation), name="fetch two locations")
]
