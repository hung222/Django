from django.shortcuts import render
from django.http import HttpResponseRedirect
from .form import RegistrationForm

def index(request):
    return render(request, 'pages/home.html')
def contact(request):
    return render(request, 'pages/contact.html')
def error404(request, exception):
    return render(request, "pages/error.html")
def error500(request):
    return render(request, "pages/error.html")
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        # Call clean_username function and clean_password function 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, 'pages/register.html', {'form':form})