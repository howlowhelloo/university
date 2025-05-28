from django.shortcuts import render
from .models import Peer

def app2_me(request):

    student = {
        "full_name": "Маетная Дарья Вадимовна",
        "photo": "/static/app2/dasha.jpg",  
        "email": "dvmaetnaya@edu.hse.ru",
        "phone": "+7 (901) 220-29-20",
        "resume": "/static/app2/resume.jpg"
    }


    context = {
        "student": student,
    }

    return render(request, 'app2/me.html', context)



def program_management(request):
    program = {
        "name": "Юриспруденция",
        "description": "Частное право и экономика",
        "lilmanager": {
            "full_name": "Демченко Елизавета Васильевна",
            "photo": "/static/app2/liza.jpg",
            "email": "edemchenko@hse.ru"
        },
        "manager": {
            "full_name": "Касаткина Александра Сергеевна",
            "photo": "/static/app2/kasatkina.jpg",
            "email": "akasatkina@hse.ru"
        }
    }
    return render(request, 'app2/management.html', {'program': program})



def app2_program(request):
    return render(request, 'app2/program.html')



def app2_peers(request):
    sort = request.GET.get('sort')
    if sort == 'za':
        classmates = Peer.objects.all().order_by('-full_name')
    else:
        classmates = Peer.objects.all().order_by('full_name')
    return render(request, 'app2/peers.html', {'peers': classmates})


