
from django.urls import path
from .views import home
urlpatterns = [
    path('app2/',home)
]