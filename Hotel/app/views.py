"""
Definition of views.
"""

from datetime import datetime
from app.models import *
from app.postgres import nationality_functions, user_functions, user_type_functions, user_info_functions, rooms_functions 
from django.contrib import messages
from django.contrib.auth.views import logout
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext


def sign_up(request):
    if request.method == "GET":
        all_nationality = Nationality.objects.all()
        return render(request, 'app/signup.html', {'all_nationality': all_nationality})
    elif request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        cellphone = request.POST.get('cellphone')
        birthday = request.POST.get('birthday')
        gender = request.POST.get('gender')

        # Get user type data
        nationality_id = request.POST.get('nationality')
        last_address = request.POST.get('last_address')
        identification_number_passport = request.POST.get('identification_number_passport')
        identification_number_citizen_card = request.POST.get('identification_number_citizen_card')
        resident = request.POST.get('resident')

        if identification_number_citizen_card == "":
            identification_number = identification_number_passport
        else:
            identification_number = identification_number_citizen_card

        # Get user data
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        description = request.POST.get('description')

        if user_functions.find_user(user_name) is not None: 
            messages.error(request,'User already registed, please try again')
            return HttpResponseRedirect('/signup')

        elif password != password2:
            messages.error(request, "password don't match")
            return HttpResponseRedirect('/signup')

        else:
            try:
                user_type = user_type_functions.create_user_type(identification_number, resident, last_address, nationality_id)
                user = user_functions.create_user(user_name, password, description)
                user_info = user_info_functions.create_user_info(first_name, last_name, email, telephone, cellphone, gender, birthday, identification_number)
                messages.success(request,'user registered')
                return HttpResponseRedirect('/')
            except Exception:
                messages.error(request,'user not registered')
                return HttpResponseRedirect('/signup')


def login(request):
    if request.method == "GET":
        return render(request, 'app/index.html')
    else:
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        validation = user_functions.validate_login(user_name, password)

        if validation is True:
            userData = user_functions.find_all_user_data(user_name)
            return render_to_response('app/profile.html',{'userData': userData})
        else:
            messages.error(request, 'Username or password is wrong, try again')
            return HttpResponseRedirect('/')


def logout(request):
    logout(request)


def profile(request):
    try:
        userData = user_functions.find_all_user_data(userData.user.user_name)
        return render_to_response('app/profile.html', {'userData': userData})
    except Exception:
        messages.error(request,'Please login to access your profile')
        return HttpResponseRedirect('/')

def rooms_details(request, room_id):
    room = rooms_functions.find_all_room_data(room_id)
    return render_to_response('app/roomsdetails.html',{'room': room})


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
