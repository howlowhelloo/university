from django.urls import path
from . import views
from .views import program_management

urlpatterns = [
    path('', views.app2_me, name='app2_me'),
    path('program/', views.app2_program, name='app2_program'),
    path('management/', views.program_management, name='program_management'),
    path('peers/', views.app2_peers, name='app2_peers'),
]
