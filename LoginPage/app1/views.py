from django.shortcuts import redirect, render
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.views.decorators.cache import never_cache

# Create your views here.

@never_cache
def user_Login(request):
    if 'username' in request.session:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request,username = username,password = pass1)
        if user :
            request.session['username']=username
            return redirect('home')
        else:
            msg = 'wrong username or password!!!'
            return render(request,'login.html',{'msg':msg})
    return render(request,'login.html')
    

@never_cache
def Home(request):
    if 'username' in request.session:
        return render(request,'home.html')
    else:
        return redirect('user_login')

@never_cache
def user_logout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect("user_login")

