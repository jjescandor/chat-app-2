from djangochat.urls import path
from .views import home

urlpatterns = [
    path("", home, name="")
]