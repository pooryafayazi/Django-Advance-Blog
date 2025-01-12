from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Post
# Create your views here.


def indexView(request):
    '''
    Function based view for index page.
    '''
    context = {'name': 'ali'}
    return render(request, 'index.html', context)


class IndexView(TemplateView):
    '''
    Class based view for index page.
    '''
    template_name = 'index.html'
    extra_context = {'name': 'reza'}
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "hassan"
        context["posts"] = Post.objects.all()
        return context