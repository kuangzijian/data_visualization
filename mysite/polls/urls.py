from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('data', views.get_all_data, name='fetch all'),
    path('distData', views.getDistinctValue, name="fetch Year range"),
    path('getLocation', csrf_exempt(views.getVaccinationForTwoLocation), name="fetch two locations")
]
