from django.urls import path
from . import views
app_name = 'server'

urlpatterns = [
    path('404', views.pageNotFound, name='404'),
    path('500', views.page_error, name='500'),
    path('about', views.about, name='about'),
]