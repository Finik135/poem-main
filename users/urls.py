from django.urls import path

from .views import authorize
from .views import registrate
from .views import logout_view


urlpatterns = [
    path("authorization/", authorize, name="authorization"),
    path("registration/", registrate, name="registration"),
    path("logout", logout_view, name="logout")
]
