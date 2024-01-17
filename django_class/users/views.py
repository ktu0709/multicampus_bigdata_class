from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render,redirect
from .forms import LoginForm

# Create your views here.
def sign_in(request):
        if(request.method) =="GET":
            form = LoginForm()
            return render(request,'login.html',{'form':form})

        elif(request.method) =="POST":
                form = LoginForm(request.POST)

                if form.is_valid():
                    username=form.cleaned_data['username']
                    passoword = form.cleaned_data['password']
                    user = authenticate(request,username=username,password=passoword)
                    if user:
                        login(request,user)
                        messages.success(
                            request,f'Hi {username.title()},welcome back!'
                        )
                        return redirect('posts')
                messages.error(request,f'Invalid username or password')
                return render(request,'login.html',{'form':form})


def sign_out(request):
    logout(request)
    messages.success(request,f'로그아웃 됨')
    return redirect('login')