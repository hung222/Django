from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/home.html')
def contact(request):
    return render(request, 'pages/contact.html')
def error404(request, exception):
    return render(request, "pages/error.html")
def error500(request):
    return render(request, "pages/error.html")