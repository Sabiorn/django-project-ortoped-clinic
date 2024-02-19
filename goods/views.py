from django.shortcuts import render, get_object_or_404
from .models import Service, Staff, Categories


def service(request):
    context = {
        "title": "Наши сотрудники",
        "staff": Staff.objects.all(),  
    }

    return render(request, "goods/service.html", context)


def catalog(request, category_slug=None):
    if category_slug == "all":
        services = Service.objects.all()
        category_name = "Все категории"
    else:
        category = get_object_or_404(Categories, slug=category_slug)
        services = Service.objects.filter(category=category)
        category_name = category.name
    
    context = {
        "title": f"Услуги по категории {category_name}",
        "services": services,
    }
    return render(request, "goods/catalog.html", context)
