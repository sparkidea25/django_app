from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse



def home(request):
    return render(request, "home.html")


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user_details = User.objects.get(username = username)
            user = authenticate(request, username=username, password=password) # Check the username and password
            if user is not None:
                login(request, user) # Login the user and return Http response.
                return HttpResponse("Login Success")
            else:
                return render(request, 'login.html', {'message': 'Invalid Credentials'})
        except ObjectDoesNotExist:
            return render(request,'login.html', {'message': 'User does not exist'})

    context = {}
    return render(request,'login.html', context=context)

def register_page(request):
     if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, "Username already taken!")
            return redirect('/register/')
     
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email
        )
     
        user.set_password(password)
        user.save()

        messages.info(request, "Account created Successfully!")
        return redirect('/register/')
     return render(request, 'register.html')

