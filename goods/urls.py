from django.urls import path

from goods import views

app_name = 'goods'

urlpatterns = [
    # path('catalog/', views.catalog, name='catalog'),
    path('catalog/<slug:category_slug>/', views.catalog, name='catalog'),  # Добавлен путь для вывода услуг по категориям
    path('service/', views.service, name='service'),
]
