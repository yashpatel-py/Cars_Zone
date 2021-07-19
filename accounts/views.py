from django.shortcuts import redirect, render
from django.contrib import messages

# Create your views here.
def login(request):
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        messages.error(request, 'There was an error processing your request.')
    return render(request, 'accounts/register.html')

def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def logout(request):
    return redirect('home')