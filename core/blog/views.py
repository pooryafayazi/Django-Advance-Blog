from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView,RedirectView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from .models import Post
# Create your views here.

# function based view show a template
"""
def indexView(request):
    '''
    Function based view for index page.
    '''
    context = {'name': 'ali'}
    return render(request, 'index.html', context)
"""

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
    
# function based view for redirecting to itmeter page
"""
def redirecttoitmeter(request):
    '''
    Function based view for redirecting to itmeter page.
    '''
    return redirect('https://itmeter.ir')
"""

# class based view for redirecting to itmeter page
class Redirecttoitmeter(RedirectView):
    url = 'https://itmeter.ir'

    def get_redirect_url(self, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs['pk'])
        print(post)
        return super().get_redirect_url(*args, **kwargs)
    

class PostList(ListView):
    #model = Post
    # queryset = Post.objects.all()
    context_object_name = 'posts'

    # paginate_by = 2
    # ordering = ['-created_date']
    def get_queryset(self):
        posts = Post.objects.filter(status='True')
        return posts