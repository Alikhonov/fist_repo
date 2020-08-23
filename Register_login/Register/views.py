from django.shortcuts import render
from Register.forms import UserForm, UserProfileInfoForm
from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'index.html',)

def registration(request):
    user_form = UserForm()
    profile_form = UserProfileInfoForm()
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pictures' in request.FILES:
                profile.profile_pictures = request.FILES['profile_pictures']

            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'register.html',
                            {'user_form':user_form,
                             'profile_form':profile_form,
                              'registered':registered})


def logging_in(request):
    if request.method == "POST":
        password = request.POST.get('username')
        username = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('account is not active')
        else:
            print('someone  tried to login')
    return render(request,'login.html',context={})

@login_required
def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
