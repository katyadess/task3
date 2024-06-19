from django.shortcuts import render

# Create your views here.


def main(request):
    return render(request, 'car_app/main.html')


def toyota(request):
    context = {
        'company': 'Toyota',
        'description': 'Toyota Motor Corporation — японская транснациональная корпорация, производитель автомобилей со штаб-квартирой в Тойота, Айти, Япония. Основана в 1937 году Киитиро Тоёда.',
        'history': 'Компания была основана в 1937 году как дочерняя компания Toyota Industries, производителя автоматических ткацких станков. Одним из ключевых моментов в истории компании стало создание первой модели легкового автомобиля — Toyota AA в 1936 году.',
        'models': ['Toyota Corolla', 'Toyota Camry', 'Toyota RAV4', 'Toyota Prius'],
        'innovations': 'Toyota известна своими инновациями в области гибридных автомобилей. Модель Toyota Prius, выпущенная в 1997 году, стала первым в мире массовым гибридным автомобилем.',
        'facts': [
            'Toyota производит более 10 миллионов автомобилей в год.',
            'В 2020 году Toyota заняла первое место по продажам среди всех автомобильных компаний.',
            'Компания активно развивает технологии автономного вождения и водородные топливные элементы.'
        ]
    }
    
    return render(request, 'car_app/toyota.html', context)
    
def honda(request):
    pass

def renault(request):
    pass