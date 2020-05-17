from django.shortcuts import render
from basic_app.forms import userForm,userProfileForm
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# from django.core.urlresolvers import reverse #old versiom
from django.urls import reverse #newer version
from django.contrib.auth import authenticate,login,logout


def index(request):
    return render(request, 'basic_app/index.html')

@login_required
def special(request):
    return HttpResponse('You are Logged In')

@login_required
def user_logout(request) :
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == "POST" :
        user_from = userForm(data = request.POST)
        profile_from = userProfileForm(data = request.POST)

        if user_from.is_valid() and profile_from.is_valid():
            user = user_from.save()
            user.set_password(user.password)
            user.save()

            profile = profile_from.save(commit = False)
            profile.user = user

            if 'profile_pic' in request.FILES :
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True

        else:
            print(user_from.errors, profile_from.errors)

    else:
        user_from = userForm()
        profile_from = userProfileForm()
        # registered = True

    return render(request, 'basic_app/registration.html',
                            {'user_from':user_from,
                            'profile_form':profile_from,
                            'registered':registered})


def user_login(request):
    if request.method == "POST" :
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user :
            if user.is_active :
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else :
                return HttpResponse('Account Not Active')

        else :
            print("Someone tried to login from your Account")
            print('Details :')
            print('username : {}'.format(username))
            print('password : {}'.format(password))

    else :
        return render(request,'basic_app/login.html',context = None)
