from django.urls import path

from goods import views

app_name = 'goods'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('service/', views.service, name='service'),
]