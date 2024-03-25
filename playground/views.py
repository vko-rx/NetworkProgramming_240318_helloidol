from django.http import HttpResponse
from django.shortcuts import render

def say_hello(request):
    return HttpResponse("Hello World")

def say_hello_html(request):
    return render(request, 'playground/hello.html', {'name': '지우야',
                                                     'greeting': '안녕~'})

def say_bye_html(request):
    context = {
        'singer': 'WOODZ',
        'title': 'Drowning',
    }
    return render(request, 'playground/bye.html', context = context)
