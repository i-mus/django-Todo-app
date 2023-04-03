from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('accounts:login')


def register(request):
    if request.method == 'POST':
        un = request.POST['user_name']
        fn = request.POST['first_name']
        ln = request.POST['last_name']
        email = request.POST['email_id']
        password = request.POST['pass1']
        cpassword = request.POST['pass2']
        if User.objects.filter(username=un).exists():
            messages.info(request, "Username already taken")
            return redirect('accounts:register')
        elif User.objects.filter(email=email).exists():
            messages.info(request, "email already taken")
            return redirect('accounts:register')
        elif password == cpassword:
            user = User.objects.create_user(username=un, email=email, first_name=fn, last_name=ln, password=password)
            user.save()
            print("user created")
        else:
            messages.info(request, "password don't match")
            return redirect('accounts:register')
        return redirect('accounts:login')
    return render(request, 'registration/register.html')


def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['password']
        user = auth.authenticate(username=uname, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid user")
            return redirect('accounts:login')
    return render(request, 'registration/login.html')
