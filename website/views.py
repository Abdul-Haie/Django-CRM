from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Record

# Create your views here.
def home(request):

    records = Record.objects.all()
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']  # Use 'password1' to match the field in SignUpForm
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in")
            return redirect('home')
        else:
            messages.error(request, "There is a problem with logging in, try again.")  # Change to error message
    return render(request, 'home.html', {'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out....")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':  # Corrected typo 'mothod' to 'method'
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and Log in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You have successfully registered")
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})
