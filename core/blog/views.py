from django.shortcuts import render

# Create your views here.


def indexView(request):
    context = {'name': 'ali'}
    return render(request, 'index.html', context)