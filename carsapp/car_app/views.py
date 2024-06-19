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
    context = {
        'company': 'Honda',
        'description': 'Honda Motor Co., Ltd. — японская транснациональная корпорация, известная производством автомобилей, мотоциклов и силового оборудования. Основана в 1948 году Соитиро Хондой.',
        'history': 'Компания была основана в 1948 году Соитиро Хондой. Первоначально Honda производила мотоциклы и быстро завоевала популярность благодаря своим инновациям и качеству. В 1960-х годах компания начала производство автомобилей.',
        'models': ['Honda Civic', 'Honda Accord', 'Honda CR-V', 'Honda Fit'],
        'innovations': 'Honda известна своими инновациями в области двигателей и технологий. Компания активно развивает гибридные и электрические автомобили, а также технологии автономного вождения.',
        'facts': [
            'Honda является крупнейшим производителем мотоциклов в мире.',
            'В 1986 году Honda стала первым японским автопроизводителем, запустившим собственный бренд люксовых автомобилей — Acura.',
            'Компания активно работает над развитием робототехники и представила робота ASIMO в 2000 году.'
        ]
    }
    return render(request, 'car_app/honda.html', context)

def renault(request):
    context = {
        'company': 'Renault',
        'description': 'Renault S.A. — французская транснациональная компания, занимающаяся производством автомобилей, со штаб-квартирой в Булонь-Бийанкуре, Франция. Основана в 1899 году Луи Рено и его братьями Марселем и Фернаном.',
        'history': 'Компания была основана в 1899 году Луи Рено и его братьями. Renault начала свою деятельность с производства небольших автомобилей и быстро стала одной из ведущих автомобильных компаний во Франции. Renault также сыграла важную роль в разработке и производстве танков во время Первой мировой войны.',
        'models': ['Renault Clio', 'Renault Megane', 'Renault Captur', 'Renault Zoe'],
        'innovations': 'Renault известна своими инновациями в области электромобилей и автономного вождения. Модель Renault Zoe является одним из самых популярных электромобилей в Европе.',
        'facts': [
            'Renault является одним из крупнейших автопроизводителей в Европе.',
            'Компания активно развивает партнерства с другими автопроизводителями, включая Nissan и Mitsubishi.',
            'Renault имеет долгую историю участия в автоспорте, включая Формулу-1.'
        ]
    }
    return render(request, 'car_app/renault.html', context)