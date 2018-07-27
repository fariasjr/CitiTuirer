from django.shortcuts import render
from tuites.models import Tuite

def post_tuite(request):
    context = {}

    if request.method == 'POST':
        print('Enviando formulario!')
        # print(request.POST)
        content = request.POST.get('content', None)
        if (content.isspace() or content == ''):
            context['error'] = 'Tuite nao pode ta vaziu pow!'
            return render(request, 'post_tuite.html', context)
        # print(content)
        # if (content.isspace() or content == ''):
        #     context['certo'] = 'Valido, postando!'
        #     return render(request, 'post_tuite.html', context)
        else:
            import ipdb; ipdb.set_trace()
            Tuite.objects.create(
                content=content,
                author=request.user,
            )
            context['sucess_message'] = f'Seu Tuite: {tuite.content}, foi postado!'

    return render(request, 'post_tuite.html', context)