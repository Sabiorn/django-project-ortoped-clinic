from django.urls import path

from goods import views

app_name = 'goods'

urlpatterns = [
    path('catalog/<slug:category_slug>/', views.catalog, name='catalog'),
    path('service/', views.staff, name='index'),      #Персонал
    path('service/<slug:slug>/', views.staff, name='service'),     #услуги Добавлен путь для вывода услуг по категориям
]
