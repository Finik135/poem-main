from django.urls import path
# from .views import receive_poem
from .views import home
from .views import poem_detail
from .views import poem_create
from django.shortcuts import redirect
from .utils.customizer import apply_theme
from .views import index

app_name = 'poems'

urlpatterns = [
    path("home/", home, name="home"),
    path("create/", poem_create, name="poem_create"),
    path("<str:pk>/", poem_detail, name="poem_detail"),
    # path('api/receive_poem/', receive_poem, name='receive_poem'),
    path('set-theme/<str:theme_name>/', views.set_theme, name='set_theme'),
    path('set-theme/<str:theme_name>/', set_theme, name='set_theme'),
    path('', index, name='index')
]

def set_theme(request, theme_name):
    apply_theme(request.user, theme_name)
    return redirect('index')
