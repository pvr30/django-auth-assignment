from django.shortcuts import get_object_or_404, render, redirect
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.forms import forms
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='login')
def home(request):
    users = User.objects.all()
    data = {
        'users': users
    }
    return render(request, 'home.html', data)


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']
        password = request.POST['password1']
        confirm_password = request.POST['password2']

        if password == confirm_password:
            # check if username already exists or not
            if User.objects.filter(username=username).exists():
                return redirect("signup")
            else:
                if User.objects.filter(email=email).exists():
                    return redirect("signup")
                else:
                    user = User.objects.create_user(username=username,
                                                email=email, address= address, password=password)
                    user.save()
                    return redirect("login")
    return render(request, 'signup.html')



def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            
            return redirect('login')
    return render(request, 'login.html')

def userlogout(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def edituser(request, id):
    user = get_object_or_404(User, id=id)

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        address = request.POST['address']

        user.username=username
        user.email = email
        user.address = address
        user.save()
        return redirect('logout')
        
    data = {
        'user':user
    }
    return render(request, 'edit.html', data)

@login_required(login_url='login')
def deleteuser(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('signup')