from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from tuites.forms import PostTuiteForm
from tuites.models import Tuite


class PostTuiteView(LoginRequiredMixin,CreateView):
    model = Tuite
    template_name = 'post_tuite.html'
    form_class = PostTuiteForm
    success_url = reverse_lazy('tuites:post_tuite')

    def get_initial(self):
        return {
            'user': self.request.user
        }

    def form_valid(self, form):
        messages.success(
            self.request,
            'Vc postou!'
        )
        return super().form_valid(form)



#LIXUUUU
# def post_tuite(request):
#     context = {}

#     if request.method == 'POST':
#         print('Enviando formulario!')
#         # print(request.POST)
#         content = request.POST.get('content', None)
#         if (content.isspace() or content == ''):
#             context['error'] = 'Tuite nao pode ta vaziu pow!'
#             return render(request, 'post_tuite.html', context)
#         # print(content)
#         # if (content.isspace() or content == ''):
#         #     context['certo'] = 'Valido, postando!'
#         #     return render(request, 'post_tuite.html', context)
#         else:
#             import ipdb; ipdb.set_trace()
#             Tuite.objects.create(
#                 content=content,
#                 author=request.user,
#             )
#             context['sucess_message'] = f'Seu Tuite: {tuite.content}, foi postado!'

#     return render(request, 'post_tuite.html', context)
