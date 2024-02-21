from django.shortcuts import render, get_object_or_404
from goods.models import Service, Staff, Categories



def staff(request, category_slug=None):
    category = None
    if category_slug:
        category = get_object_or_404(Categories, slug=category_slug)
        staff = Staff.objects.filter(category=category)
    else:
        staff = Staff.objects.all()

    context = {
        "title": "Наши сотрудники",
        "staff": staff,
        "category": category  # передаем категорию в контекст
    }
    return render(request, "goods/service.html", context)




def catalog(request, category_slug=None):
    if category_slug == "all":
        category_name = "Все категории"
        category_description = "Описание всех категорий"
        services = Service.objects.all()
        staff = Staff.objects.all()
    else:
        category = get_object_or_404(Categories, slug=category_slug)
        category_name = category.name
        category_description = category.description  # Получаем описание категории
        services = Service.objects.filter(category=category)
        staff = Staff.objects.filter(category=category)
    
    context = {
        "title": f"Услуги по категории {category_name}",
        "category_name": category_name,
        "category_description": category_description,  # Передаем описание категории в контекст
        "services": services,
        "staff": staff
    }
    return render(request, "goods/catalog.html", context)

