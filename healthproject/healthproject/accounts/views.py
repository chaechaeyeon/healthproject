from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

def signup(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['repeat']:
            new_user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'], email=request.POST['email'],)
          
            auth.login(request, new_user,  backend='django.contrib.auth.backends.ModelBackend')
            print('회원가입 성공')
            return redirect('index')
    return render(request,'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            print('로그인 성공')
            return redirect('index')
        else: 
            return render(request, 'bad_login.html')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('index')