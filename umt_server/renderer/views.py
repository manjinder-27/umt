from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from api.models import Monitor

def home_page(request):
    return render(request,'home.html')

def login_page(request):
    if request.method == 'POST':
        try:
            user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
            if user is not None:
                login(request,user)
                return redirect('dashboard')
            return render(request,'login.html',{'error_msg':'Invalid Credentials'})
        except:
            return render(request,'login.html',{'error_msg':'Try again !'})
    return render(request,'login.html')

def signup_page(request):
    if request.method =='POST':
        try:
            if request.POST['password'] != request.POST['confirm_password']:
                return render(request,'signup.html',{'error_msg':'Passwords do not match'})
            if User.objects.filter(username=request.POST['username']).exists():
                return render(request,'signup.html',{'error_msg':'Username already exists'})
            new_user = User.objects.create_user(first_name=request.POST['first_name'],last_name=request.POST['last_name'],username=request.POST['username'],email=request.POST['email'],password=request.POST['password'])
            login(request,new_user)
            return redirect('dashboard')
        except:
            return render(request,'signup.html',{'error_msg':'Try again !'})
    return render(request,'signup.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'dashboard.html')
    else:
        return redirect('login_page')

def add_monitor(request):
    if request.method == 'POST':
        try:
            new_monitor = Monitor(user=request.user,name=request.POST['name'],url=request.POST['url'],interval=request.POST['interval'],expected_status=request.POST['expected_status'])
            new_monitor.save()
            return redirect('dashboard')
        except:
            return redirect('dashboard')
    return render(request,'add_monitor.html')

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')
