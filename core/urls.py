from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pastes', views.show_pastes, name='pastes'),
    path('<slug:slug>', views.paste_detail, name='paste-detail')
]


