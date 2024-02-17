from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     context = {
#         'title': 'Медицинский Центр неврологии и ортопедии'}
#     return render(request, 'main/index.html', context)

def index(request):
    context = {
        'title': 'Медицинский Центр неврологии и ортопедии',
        # 'services': Service.objects.all()  # Получаем все объекты модели Service
    }
    return render(request, 'main/index.html', context)


def about(request):
    context = {
        'title': 'О нас',
        'content': "О нас",
        'text_on_page': """Наш медицинский центр открылся в 2015 году.  Основатель центра врач травматолог-ортопед Малик Андрей Юрьевич.
На сегодняшний день «Медицинский центр неврологии и ортопедии» возглавляет врач-невролог Малик Ксения Валерьевна.   
У нас работают высококвалифицированные специалисты, центр оснащен современной аппаратурой для оказания  диагностической и консультативной помощи, а также проведения реабилитации пациентов.   
Прием ведут врачи высшей категории , регулярно повышающие уровень своей квалификации.  
 В составе центра работает специализированный оздоровительно-тренажерный зал."""
    }

    return render(request, 'main/about.html', context)
