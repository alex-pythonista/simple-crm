from django.urls import path

from .views import *

urlpatterns = [
    path('', lead_list),
    path('<pk>/', lead_datail, name='lead-detail'),

]