from django.shortcuts import render, get_object_or_404
from .models import Service, Staff, Categories


# def staff(request):
#     staff = Staff.objects.all()
#     context = {
#         "title": "Наши сотрудники",
#         "staff": staff,  
#     }
#     return render(request, "goods/service.html", context)


def staff(request, slug=None):
    if slug:
        # Если slug передан, пытаемся получить сотрудника по slug
        employee = get_object_or_404(Staff, slug=slug)
        context = {
            "title": f"{employee.name}",
            "employee": employee
        }
        return render(request, "goods/staff_detail.html", context)
    else:
        # Если slug не передан, отображаем список всех сотрудников
        staff_list = Staff.objects.all()
        context = {
            "title": "Наши сотрудники",
            "staff": staff_list,
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
