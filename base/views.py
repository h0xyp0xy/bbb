from django.shortcuts import render, HttpResponse

from .models import Message
from analytics.models import Funnel


def payments_http(request):

    if request.METHOD == 'POST':
        pass


""" 
185.71.76.0/27
185.71.77.0/27
77.75.153.0/25
77.75.156.11
77.75.156.35
77.75.154.128/25
2a02:5180::/32 """










def l(request):

    if request.user.is_authenticated:

        u = True

    else:

        u = False

    if not Funnel.objects.filter(stage = '0').filter(ip = request.headers['host']).exists():

        Funnel.objects.create(

            stage = '0',
            ip = request.headers['host'],

        )

    return render(request, 'landing.html', {'u': u, 'ip': request.headers['host']})

# Contact

def c(request):
    
    if request.user.is_authenticated:
        
        return render(request, 'contact.html', {'n': request.user.profile.name, 'u': request.user})
    
    else:
        
        return render(request, 'contact.html', {'u': request.user})
    
# contact submit
def cs(request):
    
    if request.user.is_authenticated:
        
        Message.objects.create(
            
            user = request.user,

            topic = request.POST.get('t'),
            message = request.POST.get('m'),
            
        )
        
    else:
        
        Message.objects.create(
            
            name = request.POST.get('n'),
            email = request.POST.get('e'),
            
            topic = request.POST.get('t'),
            message = request.POST.get('m'),

        )
    
    return HttpResponse('K')

# Info

def t(request):

    if request.user.is_authenticated:

        u = True

    else:

        u = False

    return render(request, 'info/terms.html', {'u': u})

def p(request):

    if request.user.is_authenticated:

        u = True

    else:

        u = False

    return render(request, 'info/privacy.html', {'u': u})

def j(request):

    if request.user.is_authenticated:

        u = True

    else:

        u = False

    c = {}

    c['u'] = u

    return render(request, 'info/juridical.html', c)

def ds(request):

    if request.user.is_authenticated:

        u = True

    else:

        u = False

    c = {}

    c['u'] = u

    c['d'] = Info.objects.get(title = 'Безопасность данных')
    c['i'] = 'ds'

    return render(request, 'info/terms.html', c)

def ps(request):

    if request.user.is_authenticated:

        u = True

    else:

        u = False

    c = {}

    c['u'] = u

    c['d'] = Info.objects.get(title = 'Безопасность онлайн платежей')
    c['i'] = 'ps'

    return render(request, 'info/terms.html', c)

def plans(request):

    if request.user.is_authenticated:

        u = True

    else:

        u = False

    c = {}

    c['u'] = u

    return render(request, 'info/plans.html', c)

