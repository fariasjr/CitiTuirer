from django.shortcuts import render
from django.http import HttpResponse
from .helpers import get_character_name, ip_info
from datetime import datetime
#from random import randint

# Create your views here.

def index(request):
    #nome = '<b>Farias</b>'
    #return HttpResponse(f'Sua pagina carregou {nome}.')
    #import ipdb; ipdb.set_trace() #breack-point 
    
    #id_random = randint(0,20)
    #print(id2)
    
    #nome = get_character_name(id_random)
    #return HttpResponse(f'Ola, tudo bem {nome}')
    
    # country = ip_info('country_name')
    # flag = ip_info('flag')
    # flag_image = f'<img src="{flag}" width=120" />'

    #return HttpResponse(
    #    f'Oi, como vai o <b>{country}</b>?<br>{flag_image}'
    #)

    context = {
        # 'my_name': 'Julia',
        # 'country_name': country,
        # 'flag_image': flag_image,
        'now': datetime.now()

    }

    return render(request, 'home.html', context)