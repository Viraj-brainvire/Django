from django.shortcuts import render , redirect
from django.contrib.auth import login , logout , authenticate
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == 'POST':
        username  = request.POST['username']  
        password  = request.POST['password']
        # Authenticate
        user = authenticate(request , username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have Been Logged In!')
            return redirect('home')
        else:
            messages.success(request, 'There was a error in Logging In , Incorrect Password or username ...')
            return redirect('home')
    else:
        return render(request,'home.html',{})

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request,"You have been Logged out ..." )
    return redirect('home')

def register_user(request):
    return render(request, 'register.html')