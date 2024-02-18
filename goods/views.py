from django.shortcuts import render

from goods.models import Service, Staff


def catalog(request):
    context = {
        "title": "Наши услуги",
        "services": Service.objects.all(),  # Получаем все объекты модели Service
    }
    return render(request, "goods/catalog.html", context)


def service(request):
    context = {
        "title": "Наши сотрудники",
        "staff": Staff.objects.all(),  
    }

    return render(request, "goods/service.html", context)
