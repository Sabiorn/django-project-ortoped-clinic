from django.urls import path

from goods import views

app_name = 'goods'

urlpatterns = [
    path('catalog/', views.catalog, name='catalog'),
    path('service/', views.service, name='service'),
]