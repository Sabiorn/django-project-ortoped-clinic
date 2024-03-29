from django import template
from goods.models import Categories, Service, Staff

register = template.Library()

@register.simple_tag()
def tag_categories():
    return Categories.objects.all()

@register.simple_tag()
def tag_staff():
    return Staff.objects.all()

@register.simple_tag()
def tag_service():
    return Service.objects.all()
