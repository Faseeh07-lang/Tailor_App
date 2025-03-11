from django.urls import path
from .views import create_customer, enter_size

urlpatterns = [
    path('', create_customer, name='create_customer'),
    path('enter-size/', enter_size, name='enter_size'),
]

