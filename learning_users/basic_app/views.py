from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm

# For login-logout
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save() # saving form to database
            user.set_password(user.password) # hashing the password
            user.save()                      # then again saving the form data into the database

            profile = profile_form.save(commit=False)
            profile.user = user     # defining one-to-one relation

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    context_dict = {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
    return render(request, 'basic_app/registration.html', context_dict)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Django built-in authentication function
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                # Log the user in
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                HttpResponse('Your account is not active')
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse('Invalid login details supplied.')
    else:
        return render(request, 'basic_app/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse('You are logged in.')
