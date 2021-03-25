from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('documents/', views.documents, name='documents'),
    path('personnel/', views.personnel, name='personnel'),
    path('research/', views.research, name='research'),
    path('publications/', views.publications, name='publications'),
    path('database/', views.database, name='database'),
    path('outreach/', views.outreach, name='outreach')
]
