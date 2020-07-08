from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'mysite/index.html')

def resume(request):
    return render(request, 'mysite/resume.html')

def about(request):
    return render(request, 'mysite/about.html')

def matlab(request):
    return render(request, 'mysite/matlab.html')

def web(request):
    return render(request, 'mysite/web.html')

def proteus(request):
    return render(request, 'mysite/proteus.html')