from django.urls import path
# from .views import receive_poem
from .views import home
from .views import poem_detail
from .views import poem_create
from .views import index
from . import views



# app_name = 'poems'

urlpatterns = [
    path("home/", home, name="home"),
    path("create/", poem_create, name="poem_create"),
    path("<str:pk>/", poem_detail, name="poem_detail"),
    # path('api/receive_poem/', receive_poem, name='receive_poem'),
    path('set-theme/<str:theme_name>/', views.set_theme, name='set_theme'),
    path('', index, name='index')
]


